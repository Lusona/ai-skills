#!/usr/bin/env python3
"""Build a portable catalog from the canonical plugins/lusona sources."""

import argparse
import json
import re
import shutil
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = Path('plugins/lusona')
CATALOGS = (Path('.agents/plugins/marketplace.json'), Path('.claude-plugin/marketplace.json'),
            Path('.cursor-plugin/marketplace.json'))


def check_links(root):
    for file in root.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', file.read_text()):
            if '://' not in target and not (file.parent / target.split('#')[0]).exists():
                raise ValueError(f'Broken resource link: {file}: {target}')


def check_skill_templates(source):
    templates = (source / 'templates').resolve()
    for skill in (source / 'skills').glob('*/SKILL.md'):
        targets = re.findall(r'\]\(([^)]+)\)', skill.read_text())
        if not any('://' not in target
                   and (skill.parent / target.split('#')[0]).resolve().parent == templates
                   and (skill.parent / target.split('#')[0]).is_file()
                   for target in targets):
            raise ValueError(f'Skill must link an existing output template: {skill}')


def build(output):
    source = ROOT / PLUGIN
    if (ROOT / 'LICENSE').read_bytes() != (source / 'LICENSE').read_bytes():
        raise ValueError('Repository and plugin LICENSE files must match.')
    check_skill_templates(source)
    codex = json.loads((source / '.codex-plugin/plugin.json').read_text())
    claude = json.loads((source / '.claude-plugin/plugin.json').read_text())
    cursor = json.loads((source / '.cursor-plugin/plugin.json').read_text())
    manifests = (codex, claude, cursor)
    if any(manifest['name'] != PLUGIN.name for manifest in manifests):
        raise ValueError('Native manifest names must match the plugin directory.')
    if (any(manifest['version'] != codex['version'] for manifest in manifests)
            or not re.fullmatch(r'\d+\.\d+\.\d+', codex['version'])):
        raise ValueError('Native manifest versions must match and use major.minor.patch.')
    catalogs = [json.loads((ROOT / path).read_text()) for path in CATALOGS]
    if any(catalog['name'] != 'lusona-ai-skills' for catalog in catalogs):
        raise ValueError('All catalogs must be named lusona-ai-skills.')
    for catalog in catalogs:
        if len(catalog['plugins']) != 1:
            raise ValueError('Update the package file selection before adding more plugins.')
        entry = catalog['plugins'][0]
        location = entry['source']
        if isinstance(location, dict):
            if location['source'] != 'local':
                raise ValueError('Codex catalog source must be local.')
            location = location['path']
        if entry['name'] != codex['name'] or location != './plugins/lusona':
            raise ValueError('Catalog entry must point to ./plugins/lusona.')
    if output.exists():
        raise ValueError(f'Output already exists: {output}. Choose a new output directory.')

    catalog = output / 'lusona-ai-skills'
    plugin = catalog / PLUGIN
    plugin.mkdir(parents=True)
    # Explicit selection excludes consuming projects and their live queues.
    for name in ('README.md', 'LICENSE', '.codex-plugin/plugin.json',
                 '.claude-plugin/plugin.json', '.claude-plugin/icon.png',
                 '.cursor-plugin/plugin.json'):
        destination = plugin / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source / name, destination)
    for name in ('skills', 'templates', 'scripts', 'references'):
        shutil.copytree(source / name, plugin / name)
    for relative in (*CATALOGS, *(Path(name) for name in (
        'README.md', 'README.es.md', 'README.de.md', 'README.zh-CN.md', 'README.ja.md',
        'CONTRIBUTING.md', 'INSTALL.md', 'LICENSE', 'scripts/package.py',
    ))):
        destination = catalog / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, destination)
    check_links(catalog)
    archive = output / f"{codex['name']}-{codex['version']}.zip"
    with ZipFile(archive, 'w', compression=ZIP_DEFLATED) as bundle:
        for file in sorted(catalog.rglob('*')):
            if file.is_file():
                bundle.write(file, file.relative_to(output))
    return catalog, plugin, archive


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'tmp/lusona-package',
                        help='New output directory; defaults to repository-local tmp/lusona-package.')
    args = parser.parse_args()
    try:
        catalog, plugin, archive = build(args.output.expanduser().resolve())
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f'Package build failed: {error}\n')
    print(f'Catalog: {catalog}\nPlugin: {plugin}\nArchive: {archive}')
    print('No harness configuration or project data was changed.')


if __name__ == '__main__':
    main()
