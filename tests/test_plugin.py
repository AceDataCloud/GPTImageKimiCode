import json
from pathlib import Path
import unittest
from urllib.parse import urlparse, parse_qs

ROOT = Path(__file__).resolve().parents[1]

class PluginContract(unittest.TestCase):
    def test_single_service_and_secret_binding(self):
        m = json.loads((ROOT / 'kimi.plugin.json').read_text())
        self.assertEqual(m['name'], 'gpt-image-by-ace')
        self.assertEqual(list(m['mcpServers']), ['gpt-image'])
        server = m['mcpServers']['gpt-image']
        self.assertEqual(server['transport'], 'stdio')
        self.assertEqual(server['command'], 'uvx')
        self.assertEqual(server['args'], ['--from', 'mcp-openai-pro==2026.10.19.2', 'mcp-openai-pro', '--profile', 'gpt-image'])
        self.assertNotIn('url', server)
        self.assertNotIn('env', server)  # inherit user process env, never bundle a key
        self.assertNotIn('headers', server)
        self.assertEqual(server['enabledTools'], ['gpt_image_generate', 'gpt_image_edit', 'gpt_image_get_task', 'gpt_image_list_tasks', 'gpt_image_list_models'])
        self.assertTrue((ROOT / m['skills'] / 'gpt-image-ace' / 'SKILL.md').is_file())
        self.assertFalse(any(k in m for k in ['tools','apps','inject','configFile','hooks']))

    def test_catalog_does_not_claim_official_status(self):
        c = json.loads((ROOT / 'docs/marketplace-candidate.json').read_text())
        self.assertEqual(len(c['plugins']), 1)
        self.assertNotIn('tier', c['plugins'][0])
        self.assertEqual(c['plugins'][0]['source'], 'https://github.com/AceDataCloud/GPTImageKimiCode/releases/tag/v0.1.0')

    def test_onboarding_links_and_assets(self):
        m = json.loads((ROOT / 'kimi.plugin.json').read_text())
        q = parse_qs(urlparse(m['interface']['websiteURL']).query)
        self.assertEqual(set(q), {'utm_source','utm_medium','utm_campaign','utm_content'})
        self.assertEqual(q['utm_source'], ['github'])
        self.assertEqual(q['utm_medium'], ['referral'])
        for f in ['get-api-key-en.png','create-api-key-en.png']:
            self.assertTrue((ROOT / 'assets/tutorial' / f).is_file())
        for file in ['README.md','readme/README_zh_Hans.md','commands/status.md']:
            self.assertTrue((ROOT / file).is_file())

if __name__ == '__main__':
    unittest.main()
