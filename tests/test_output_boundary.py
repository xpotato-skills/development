"""Regression checks for the fictional release and distributable legal metadata."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/japanese-release-notes'
FIXTURE = json.loads((ROOT / 'tests/fixtures/maple-release.json').read_text(encoding='utf-8'))


def require_output_boundary(text):
    """Assess this MIT-project fixture; never forbid another project's own terms."""
    notice = (ROOT / 'NOTICE').read_text(encoding='utf-8')
    skill_credit = re.search(r'^Project attribution and maintenance: (.+)$', notice, re.M).group(1)
    credit_names = [skill_credit, *[name.strip() for name in skill_credit.split('/')]]
    if any(name.casefold() in text.casefold() for name in credit_names) or 'japanese-release-notes' in text.casefold():
        raise ValueError('Skill identity leaked into generated release')
    if FIXTURE['project_license'] != 'AGPL-3.0-only' and 'agpl' in text.casefold():
        raise ValueError('Skill distribution terms leaked into the MIT-project fixture')
    for required in [FIXTURE['project'], FIXTURE['version'], FIXTURE['project_credit'],
                     FIXTURE['project_license'], FIXTURE['third_party_notice'],
                     FIXTURE['project_license_url'], FIXTURE['third_party_notice_url']]:
        if required not in text:
            raise ValueError('Target project fact or notice missing: ' + required)
    for asset in FIXTURE['assets']:
        if asset['url'] not in text or asset['name'] not in text:
            raise ValueError('Target download missing')


class OutputBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample = (ROOT / 'examples/maple-v1.4.0.md').read_text(encoding='utf-8')

    def test_fictional_sample_retains_project_notices_without_skill_identity(self):
        require_output_boundary(self.sample)
        self.assertIn('架空', self.sample)
        self.assertIn('未検証', self.sample)
        self.assertIn('未実施', self.sample)

    def test_rejects_skill_credit_in_output(self):
        credit = re.search(r'^Project attribution and maintenance: (.+)$', (ROOT / 'NOTICE').read_text(encoding='utf-8'), re.M).group(1)
        for name in [credit, *[part.strip() for part in credit.split('/')]]:
            for spelling in [name, name.lower()]:
                with self.subTest(credit=spelling), self.assertRaisesRegex(ValueError, 'Skill identity'):
                    require_output_boundary(self.sample + '\n' + spelling)

    def test_rejects_skill_license_in_mit_project_output(self):
        with self.assertRaisesRegex(ValueError, 'Skill distribution terms'):
            require_output_boundary(self.sample + '\nAGPL-3.0-only')

    def test_rejects_removing_target_project_notice(self):
        with self.assertRaisesRegex(ValueError, 'Target project fact'):
            require_output_boundary(self.sample.replace(FIXTURE['third_party_notice'], ''))

    def test_installed_package_preserves_standard_license_and_output_permission(self):
        for filename in ['LICENSE', 'NOTICE', 'OUTPUT-PERMISSION.md']:
            self.assertEqual((ROOT / filename).read_bytes(), (SKILL / filename).read_bytes())
        license_text = (ROOT / 'LICENSE').read_text(encoding='utf-8')
        self.assertIn('GNU AFFERO GENERAL PUBLIC LICENSE', license_text)
        self.assertIn('Version 3, 19 November 2007', license_text)
        self.assertIn('Additional permissions', license_text)
        self.assertIn('AGPL-3.0-only', (ROOT / 'NOTICE').read_text(encoding='utf-8'))

    def test_processing_instructions_do_not_embed_distribution_credit(self):
        for relative in ['SKILL.md', 'references/template.md', 'agents/openai.yaml']:
            text = (SKILL / relative).read_text(encoding='utf-8')
            self.assertNotIn('Xpotato', text)
            self.assertNotIn('AGPL-3.0-only', text)


if __name__ == '__main__':
    unittest.main()
