import json
import unittest

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    def test_users(self):
        response = self.client.get("/users/ping")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn(data["status"], "success")


if __name__ == "__main__":
    unittest.main()
