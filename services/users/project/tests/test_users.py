import json
import unittest

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    def test_users(self):
        response = self.client.get("/users/ping")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn(data["status"], "success")

    def test_add_user(self):
        with self.client:
            response = self.client.post(
                "/users",
                data=json.dumps({"username": "testuser", "email": "test@test.com"}),
                content_type="application/json",
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn(data["message"], "test@test.com was added.")
            self.assertIn(data["status"], "success")


if __name__ == "__main__":
    unittest.main()
