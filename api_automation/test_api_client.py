import unittest
from unittest.mock import patch, MagicMock
from api_automation.api_client import ApiClient


class TestApiClient(unittest.TestCase):
    """Unit tests for the ApiClient class."""

    def setUp(self):
        """Set up ApiClient for testing."""
        self.client = ApiClient()

    @patch("api_automation.api_client.requests.request")
    def test_create_user_success(self, mock_request):
        """Test successful user creation."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"userID": "12345"}
        mock_response.status_code = 201
        mock_request.return_value = mock_response

        response = self.client.create_user("testuser", "Password123!")
        self.assertEqual(response["userID"], "12345", "User creation failed!")

    @patch("api_automation.api_client.requests.request")
    def test_generate_token_success(self, mock_request):
        """Test successful token generation."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"token": "abcdefg12345"}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        token = self.client.generate_token("testuser", "Password123!")
        self.assertEqual(token, "abcdefg12345", "Token generation failed!")

    @patch("api_automation.api_client.requests.request")
    def test_list_books_success(self, mock_request):
        """Test successful retrieval of book list."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"books": [{"isbn": "1111"}, {"isbn": "2222"}]}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        books = self.client.list_books()
        self.assertEqual(len(books), 2, "Book list retrieval failed!")
        self.assertEqual(books[0]["isbn"], "1111", "Incorrect book data!")

    @patch("api_automation.api_client.requests.request")
    def test_reserve_books_success(self, mock_request):
        """Test successful reservation of books."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        isbns = ["1111", "2222"]
        self.client.reserve_books("user123", "auth_token", isbns)
        self.assertTrue(mock_request.called, "Reserve books request not made!")

    @patch("api_automation.api_client.requests.request")
    def test_get_user_details_success(self, mock_request):
        """Test successful retrieval of user details."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "userID": "12345",
            "books": [{"isbn": "1111"}, {"isbn": "2222"}],
        }
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        user_details = self.client.get_user_details("user123", "auth_token")
        self.assertEqual(user_details["userID"], "12345", "User ID does not match!")
        self.assertEqual(len(user_details["books"]), 2, "Books not retrieved correctly!")

    @patch("api_automation.api_client.requests.request")
    def test_error_handling(self, mock_request):
        """Test API client's error handling on failed request."""
        mock_request.side_effect = Exception("API request failed!")

        with self.assertRaises(Exception):
            self.client.create_user("testuser", "Password123!")


if __name__ == "__main__":
    unittest.main()
