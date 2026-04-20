import unittest
from unittest.mock import patch
from pathlib import Path
import sys

SRC_PATH = Path(__file__).resolve().parents[1] / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ops_manager_sdk.ops_manager_client import OpsManagerClient
from ops_manager_sdk.config import ClientConfig


class ClientAuthTestCase(unittest.TestCase):
    @patch("ops_manager_sdk.ops_manager_client.DigestAuth")
    @patch("ops_manager_sdk.ops_manager_client.Client")
    def test_uses_digest_auth_when_credentials_are_provided(
        self,
        client_mock,
        digest_auth_mock,
    ) -> None:
        digest_auth_instance = object()
        digest_auth_mock.return_value = digest_auth_instance

        config = ClientConfig(
            base_url="https://example.local",
            public_key="digest-user",
            private_key="digest-password",
        )

        OpsManagerClient(config)

        digest_auth_mock.assert_called_once_with("digest-user", "digest-password")
        _, kwargs = client_mock.call_args
        self.assertIs(kwargs["auth"], digest_auth_instance)
        self.assertEqual(kwargs["base_url"], "https://example.local/api/public/v1.0")

    @patch("ops_manager_sdk.ops_manager_client.DigestAuth")
    @patch("ops_manager_sdk.ops_manager_client.Client")
    def test_passes_timeout_to_http_client(self, client_mock, digest_auth_mock) -> None:
        digest_auth_mock.return_value = object()
        config = ClientConfig(
            base_url="https://example.local",
            public_key="digest-user",
            private_key="digest-password",
            timeout=12.5,
        )

        OpsManagerClient(config)

        _, kwargs = client_mock.call_args
        self.assertEqual(kwargs["timeout"], 12.5)


if __name__ == "__main__":
    unittest.main()
