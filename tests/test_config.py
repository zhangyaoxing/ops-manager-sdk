import unittest
from pathlib import Path
import sys

SRC_PATH = Path(__file__).resolve().parents[1] / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ops_manager_sdk.config import ClientConfig


class ClientConfigTestCase(unittest.TestCase):
    def test_headers_include_default_http_headers(self) -> None:
        config = ClientConfig(
            base_url="https://example.local",
            public_key="public",
            private_key="private",
        )

        headers = config.headers
        user_agent = str(headers["User-Agent"])

        self.assertEqual(headers["Accept"], "application/json")
        self.assertEqual(headers["Content-Type"], "application/json")
        self.assertTrue(user_agent.startswith("ops-manager-sdk/"))


if __name__ == "__main__":
    unittest.main()
