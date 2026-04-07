import unittest

from ops_manager_sdk.config import ClientConfig


class ClientConfigTestCase(unittest.TestCase):
    def test_headers_include_bearer_token(self) -> None:
        config = ClientConfig(base_url="https://example.local", api_token="secret-token")

        headers = config.headers()

        self.assertEqual(headers["Authorization"], "Bearer secret-token")
        self.assertEqual(headers["Accept"], "application/json")


if __name__ == "__main__":
    unittest.main()
