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
    @patch("ops_manager_sdk.client.httpx.DigestAuth")
    @patch("ops_manager_sdk.client.httpx.Client")
    def test_uses_digest_auth_when_credentials_are_provided(
        self,
        client_mock,
        digest_auth_mock,
    ) -> None:
        digest_auth_instance = object()
        digest_auth_mock.return_value = digest_auth_instance

        config = ClientConfig(
            base_url="https://example.local",
            digest_username="digest-user",
            digest_password="digest-password",
        )

        OpsManagerClient(config)

        digest_auth_mock.assert_called_once_with("digest-user", "digest-password")
        _, kwargs = client_mock.call_args
        self.assertIs(kwargs["auth"], digest_auth_instance)

    @patch("ops_manager_sdk.client.httpx.Client")
    def test_uses_no_auth_when_digest_credentials_are_missing(self, client_mock) -> None:
        config = ClientConfig(base_url="https://example.local")

        OpsManagerClient(config)

        _, kwargs = client_mock.call_args
        self.assertIsNone(kwargs["auth"])


if __name__ == "__main__":
    unittest.main()
