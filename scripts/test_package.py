#!/usr/bin/env python3
"""Behavioral checks for native manifest validation and portable contents."""

import importlib.util
import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('package', ROOT / 'scripts/package.py')
package = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(package)
ANTIGRAVITY = Path('.antigravity-plugin/plugin.json')


class PackageTests(unittest.TestCase):
    def assert_discoverable(self, catalog, name):
        plugin = catalog / package.PLUGIN
        manifests = [plugin / host / 'plugin.json' for host in
                     ('.codex-plugin', '.claude-plugin', '.cursor-plugin')]
        manifests.append(catalog / ANTIGRAVITY)
        for manifest in manifests:
            with self.subTest(manifest=manifest.relative_to(catalog)):
                skills = manifest.parent.parent / json.loads(manifest.read_text())['skills']
                commands = {entry.parent.name: entry for entry in skills.glob('*/SKILL.md')}
                self.assertIn(name, commands,
                              f'The native skills directory must expose the {name} command.')
                frontmatter = commands[name].read_text().split('---', 2)[1]
                self.assertRegex(frontmatter, rf'(?m)^name: {name}$')

    def assert_design_discoverable(self, catalog):
        self.assert_discoverable(catalog, 'design')

    def setUp(self):
        (ROOT / 'tmp').mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix='package-test-', dir=ROOT / 'tmp')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / 'source'
        self.root.mkdir()
        shutil.copytree(ROOT / package.PLUGIN, self.root / package.PLUGIN)
        for relative in (*package.CATALOGS, *(Path(name) for name in (
            'README.md', 'README.es.md', 'README.de.md', 'README.zh-CN.md', 'README.ja.md',
            'CHANGELOG.md', 'CONTRIBUTING.md', 'INSTALL.md', 'PRIVACY.md', 'TERMS.md', 'LICENSE',
            'scripts/package.py', 'scripts/test_package.py',
        ))):
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative, destination)
        self.source = self.root / package.PLUGIN
        self.manifest = self.source / ANTIGRAVITY
        self.manifest.parent.mkdir(exist_ok=True)
        version = json.loads((self.source / '.codex-plugin/plugin.json').read_text())['version']
        self.manifest.write_text(json.dumps({'name': 'lusona', 'version': version}))
        reference = self.root / ANTIGRAVITY
        reference.parent.mkdir(exist_ok=True)
        reference.write_text(json.dumps({'name': 'lusona', 'version': version,
                                        'skills': './plugins/lusona/skills'}))
        self.output = Path(self.temporary.name) / 'output'
        self.root_patch = patch.object(package, 'ROOT', self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)

    def test_canonical_antigravity_identity(self):
        manifest = ROOT / package.PLUGIN / ANTIGRAVITY
        self.assertTrue(manifest.is_file(), 'Canonical Antigravity metadata must exist.')
        native = json.loads(manifest.read_text())
        codex = json.loads((ROOT / package.PLUGIN / '.codex-plugin/plugin.json').read_text())
        self.assertEqual(native['name'], 'lusona')
        self.assertEqual(native['displayName'], 'Lusona Skills')
        self.assertEqual(native['version'], codex['version'])

    def test_design_is_discoverable_through_native_skill_directories(self):
        self.assert_design_discoverable(ROOT)

    def test_package_exposes_design_with_linked_resources(self):
        catalog, plugin, archive = package.build(self.output)
        self.assert_design_discoverable(catalog)
        skill = plugin / 'skills/design/SKILL.md'
        self.assertTrue(skill.is_file(), 'The portable package must include design.')
        targets = re.findall(r'\]\(([^)]+)\)', skill.read_text())
        resources = {(skill.parent / target.split('#')[0]).resolve()
                     for target in targets if '://' not in target}
        expected = {plugin / relative for relative in
                    ('references/visuals.md', 'templates/visual-page.html.template',
                     'templates/visual-reference.md.template')}
        self.assertTrue({path.resolve() for path in expected} <= resources)
        with ZipFile(archive) as bundle:
            for resource in resources | {skill.resolve()}:
                relative = resource.relative_to(plugin.resolve())
                self.assertTrue(resource.is_file(), str(relative))
                self.assertEqual(resource.read_bytes(), (self.source / relative).read_bytes())
                archived = (plugin / relative).relative_to(self.output).as_posix()
                self.assertEqual(bundle.read(archived), resource.read_bytes(), archived)

    def test_setup_is_discoverable_through_native_skill_directories(self):
        self.assert_discoverable(ROOT, 'setup')

    def test_package_exposes_setup_with_linked_resources(self):
        catalog, plugin, archive = package.build(self.output)
        self.assert_discoverable(catalog, 'setup')
        skill = plugin / 'skills/setup/SKILL.md'
        self.assertTrue(skill.is_file(), 'The portable package must include setup.')
        targets = re.findall(r'\]\(([^)]+)\)', skill.read_text())
        resources = {(skill.parent / target.split('#')[0]).resolve()
                     for target in targets if '://' not in target}
        expected = {plugin / relative for relative in
                    ('references/naming.md', 'references/workflow-guide.md',
                     'templates/agents-section.md.template', 'templates/work.md.template')}
        self.assertTrue({path.resolve() for path in expected} <= resources)
        # Setup creates the queue with the helper command; both shells must carry it.
        for helper in ('scripts/work-record.sh', 'scripts/work-record.ps1'):
            self.assertIn('init-queue', (plugin / helper).read_text(), helper)
        with ZipFile(archive) as bundle:
            for resource in resources | {skill.resolve()}:
                relative = resource.relative_to(plugin.resolve())
                self.assertTrue(resource.is_file(), str(relative))
                self.assertEqual(resource.read_bytes(), (self.source / relative).read_bytes())
                archived = (plugin / relative).relative_to(self.output).as_posix()
                self.assertEqual(bundle.read(archived), resource.read_bytes(), archived)

    def test_root_antigravity_reference_targets_canonical_skills(self):
        reference = ROOT / ANTIGRAVITY
        self.assertTrue(reference.is_file(), 'Root Antigravity reference must exist.')
        native = json.loads(reference.read_text())
        canonical = json.loads((ROOT / package.PLUGIN / ANTIGRAVITY).read_text())
        self.assertEqual(native['name'], canonical['name'])
        self.assertEqual(native['version'], canonical['version'])
        self.assertEqual((ROOT / native['skills']).resolve(),
                         (ROOT / package.PLUGIN / 'skills').resolve())

    def test_package_contains_root_antigravity_reference(self):
        catalog, _, _ = package.build(self.output)
        self.assertTrue((catalog / ANTIGRAVITY).is_file())
        self.assertEqual((catalog / ANTIGRAVITY).read_bytes(),
                         (self.root / ANTIGRAVITY).read_bytes())

    def test_rejects_root_antigravity_reference_mismatch(self):
        for field, value in (('name', 'other-plugin'), ('version', '0.0.0'),
                             ('skills', './unrelated-skills')):
            with self.subTest(field=field):
                reference = self.root / ANTIGRAVITY
                original = reference.read_text()
                manifest = json.loads(original)
                manifest[field] = value
                reference.write_text(json.dumps(manifest))
                output = self.output.with_name(f'output-{field}')
                with self.assertRaisesRegex(ValueError, 'Root Antigravity'):
                    package.build(output)
                self.assertFalse(output.exists())
                reference.write_text(original)

    def test_package_preserves_native_metadata_and_shared_resources(self):
        for relative in ('docs/lusona/work.md', 'tmp/private.txt'):
            unwanted = self.root / relative
            unwanted.parent.mkdir(parents=True, exist_ok=True)
            unwanted.write_text('project data')
        extra = self.source / 'docs/lusona/work.md'
        extra.parent.mkdir(parents=True, exist_ok=True)
        extra.write_text('project data')

        catalog, plugin, archive = package.build(self.output)
        selected = {Path('README.md'), Path('LICENSE'), ANTIGRAVITY,
                    Path('.codex-plugin/plugin.json'), Path('.claude-plugin/plugin.json'),
                    Path('.cursor-plugin/plugin.json')}
        for directory in ('skills', 'templates', 'scripts', 'references', 'assets'):
            selected.update(file.relative_to(self.source)
                            for file in (self.source / directory).rglob('*') if file.is_file())
        packaged = {file.relative_to(plugin) for file in plugin.rglob('*') if file.is_file()}
        self.assertEqual(packaged, selected)
        for relative in selected:
            self.assertEqual((plugin / relative).read_bytes(),
                             (self.source / relative).read_bytes(), str(relative))
        for relative in package.CATALOGS:
            self.assertEqual((catalog / relative).read_bytes(),
                             (self.root / relative).read_bytes())
        self.assertFalse((catalog / 'docs').exists())
        self.assertFalse((catalog / 'tmp').exists())
        with ZipFile(archive) as bundle:
            files = {file.relative_to(self.output).as_posix(): file.read_bytes()
                     for file in catalog.rglob('*') if file.is_file()}
            self.assertEqual(set(bundle.namelist()), set(files))
            for name, content in files.items():
                self.assertEqual(bundle.read(name), content, name)

    def test_rejects_antigravity_name_mismatch(self):
        manifest = json.loads(self.manifest.read_text())
        manifest['name'] = 'other-plugin'
        self.manifest.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, 'Native manifest names must match'):
            package.build(self.output)
        self.assertFalse(self.output.exists())

    def test_catalog_contains_package_test_runner(self):
        catalog, _, _ = package.build(self.output)
        for relative in ('scripts/package.py', 'scripts/test_package.py'):
            self.assertTrue((catalog / relative).is_file(), relative)
            self.assertEqual((catalog / relative).read_bytes(),
                             (self.root / relative).read_bytes(), relative)

    def test_rejects_antigravity_version_mismatch(self):
        manifest = json.loads(self.manifest.read_text())
        manifest['version'] = '0.0.0'
        self.manifest.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, 'Native manifest versions must match'):
            package.build(self.output)
        self.assertFalse(self.output.exists())


    def make_draft(self, relative='drafts/lusona'):
        """Copy the fixture plugin to another directory, keeping its `.template` names."""
        draft = self.root / relative
        shutil.copytree(self.source, draft)
        names = [template.name for template in (draft / 'templates').iterdir()]
        self.assertTrue(names and all(name.endswith('.template') for name in names), names)
        return draft

    def make_plain_names(self, relative='plain/lusona'):
        """Copy the fixture plugin with `.template` removed from template names and links."""
        plain = self.root / relative
        shutil.copytree(self.source, plain)
        names = [template.name for template in (plain / 'templates').iterdir()]
        for name in names:
            (plain / 'templates' / name).rename(plain / 'templates' / name.removesuffix('.template'))
        pattern = re.compile(r'(templates/(?:%s))\.template(?=[)#])'
                             % '|'.join(re.escape(name.removesuffix('.template')) for name in names))
        for file in plain.rglob('*.md'):
            file.write_text(pattern.sub(r'\1', file.read_text()))
        return plain

    def test_template_suffix_names_pass_template_and_link_checks(self):
        # Canonical templates use `name.ext.template` (A8); plain `name.ext` names still pass.
        plain = self.make_plain_names()
        for plugin in (self.source, plain):
            with self.subTest(plugin=plugin.relative_to(self.root)):
                package.check_skill_templates(plugin)
                package.check_links(plugin)
        self.assertTrue(any(name.endswith('.md.template')
                            for name in (path.name for path in (self.source / 'templates').iterdir())))
        self.assertFalse(any((plain / 'templates').glob('*.template')))

    def test_rejects_broken_link_in_template_file(self):
        draft = self.make_draft()
        template = next((draft / 'templates').glob('*.md.template'))
        template.write_text(template.read_text() + '\n[missing](missing.md)\n')
        with self.assertRaisesRegex(ValueError, 'Broken resource link'):
            package.check_links(draft)

    def test_builds_given_plugin_directory_without_unselected_directories(self):
        draft = self.make_draft()
        for relative in ('hooks/hooks.json', 'docs/lusona/work.md'):
            unwanted = draft / relative
            unwanted.parent.mkdir(parents=True, exist_ok=True)
            unwanted.write_text('not packaged')
        shared = self.root / 'shared/every-task.md'
        shared.parent.mkdir(parents=True)
        shared.write_text('not packaged')
        catalog, plugin, archive = package.build(self.output, Path('drafts/lusona'))
        self.assertEqual(plugin, catalog / package.PLUGIN)
        selected = {file.relative_to(draft) for file in draft.rglob('*') if file.is_file()
                    and file.relative_to(draft).parts[0] not in ('hooks', 'docs')}
        packaged = {file.relative_to(plugin) for file in plugin.rglob('*') if file.is_file()}
        self.assertEqual(packaged, selected)
        self.assertTrue(any(name.endswith('.md.template')
                            for name in (path.name for path in packaged)))
        for relative in packaged:
            self.assertEqual((plugin / relative).read_bytes(), (draft / relative).read_bytes())
        self.assertFalse((catalog / 'shared').exists())
        with ZipFile(archive) as bundle:
            names = bundle.namelist()
        self.assertFalse(any('/hooks/' in name or '/shared/' in name for name in names))

    def test_command_line_plugin_option_defaults_to_canonical_plugin(self):
        for argv, expected in ((['package.py'], package.PLUGIN),
                               (['package.py', '--plugin', 'drafts/lusona'], Path('drafts/lusona'))):
            with self.subTest(argv=argv), patch('sys.argv', argv + ['--output', str(self.output)]), \
                    patch.object(package, 'build', return_value=(Path(), Path(), Path())) as build:
                with patch('builtins.print'):
                    package.main()
                self.assertEqual(build.call_args.args[1], expected)


if __name__ == '__main__':
    unittest.main()
