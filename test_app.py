import os
import unittest
from unittest.mock import patch

from app import app


class PublicKeyDemoTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_exposed_key_is_public_and_browser_request_uses_it(self):
        script = self.client.get("/static/notes.js")
        self.assertEqual(script.status_code, 200)
        self.assertIn(b"demo_classroom_key_v1_not_real", script.data)
        script.close()
        response = self.client.post(
            "/api/summary",
            headers={"X-Demo-Key": "demo_classroom_key_v1_not_real"},
        )
        self.assertEqual(response.status_code, 200)

    def test_safe_response_never_sends_server_key(self):
        with patch.dict(os.environ, {"DEMO_SERVER_KEY": "server_only_test_value"}):
            response = self.client.post("/api/v2/summary")
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"server_only_test_value", response.data)
        self.assertNotIn(b"server_only_test_value", self.client.get("/").data)
        self.assertIn(b"notes-safe.js", self.client.get("/repaired").data)


if __name__ == "__main__":
    unittest.main()
