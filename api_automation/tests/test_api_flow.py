import unittest
from api_automation.api_client import APIClient


class TestAPIFlow(unittest.TestCase):
    def setUp(self):
        """Set up the API client and user credentials for testing."""
        self.client = APIClient()
        self.username = "testuser"
        self.password = "Password123!"

    def test_api_flow(self):
        """Test the complete API flow from user creation to book reservation."""

        # Step 1: Create User
        user_id = self.client.create_user(self.username, self.password)
        self.assertIsNotNone(user_id, "User creation failed: User ID is None")
        print(f"User created successfully with ID: {user_id}")

        # Step 2: Generate Token
        token = self.client.generate_token(self.username, self.password)
        self.assertIsNotNone(token, "Token generation failed: Token is None")
        print(f"Token generated successfully: {token}")

        # Step 3: Authorize User
        is_authorized = self.client.authorize_user(self.username)
        self.assertTrue(is_authorized, "Authorization failed: User is not authorized")
        print(f"User authorized successfully: {self.username}")

        # Step 4: List Books
        books = self.client.list_books()
        self.assertGreater(len(books), 0, "Book listing failed: No books available")
        print(f"Books available: {[book['title'] for book in books]}")

        # Step 5: Reserve Books
        book_isbns = [books[0]["isbn"], books[1]["isbn"]]
        reserve_response = self.client.reserve_books(book_isbns)
        self.assertIn("books", reserve_response, "Book reservation failed: Response does not contain books")
        print(f"Books reserved successfully: {book_isbns}")

        # Step 6: Verify Reserved Books in User Details
        user_details = self.client.get_user_details()
        self.assertIn("books", user_details, "User details retrieval failed: No books found in response")
        reserved_books = [book["isbn"] for book in user_details["books"]]
        self.assertEqual(reserved_books, book_isbns, "Reserved books do not match expected books")
        print(f"Reserved books verified successfully: {reserved_books}")


if __name__ == "__main__":
    unittest.main()
