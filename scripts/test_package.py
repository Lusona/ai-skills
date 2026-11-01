#!/usr/bin/env python3
"""Behavioral checks for native manifest validation and portable contents."""

import importlib.util
import json
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
    def setUp(self):
        (ROOT / 'tmp').mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix='package-test-', dir=ROOT / 'tmp')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / 'source'
        self.root.mkdir()
        shutil.copytree(ROOT / package.PLUGIN, self.root / package.PLUGIN)
        for relative in (*package.CATALOGS, *(Path(name) for name in (
            'README.md', 'README.es.md', 'README.de.md', 'README.zh-CN.md', 'README.ja.md',
            'CONTRIBUTING.md', 'INSTALL.md', 'PRIVACY.md', 'TERMS.md', 'LICENSE',
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


if __name__ == '__main__':
    unittest.main()
