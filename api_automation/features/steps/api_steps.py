from behave import *
from api_client import ApiClient
import logging
import random
import string
import time

# Configure logging for better debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_unique_username(base_username="TestUser"):
    """Generate a unique username using timestamp and random string"""
    timestamp = str(int(time.time()))
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    return f"{base_username}_{timestamp}_{random_str}"

@given('I have valid user credentials')
def step_impl(context):
    context.username = generate_unique_username()
    context.password = "Test@123#"  # Strong password that meets requirements
    context.api_client = ApiClient()
    logging.info(f"Generated unique username: {context.username}")

@when('I create the user')
def step_impl(context):
    try:
        response = context.api_client.create_user(context.username, context.password)
        context.user_id = response['userID']
        logging.info(f"User created successfully with ID: {context.user_id}")
    except Exception as e:
        logging.error(f"Failed to create user: {e}")
        raise

@when('I generate a token')
def step_impl(context):
    try:
        context.auth_token = context.api_client.generate_token(
            context.username, context.password
        )
        logging.info("Token generated successfully")
    except Exception as e:
        logging.error(f"Failed to generate token: {e}")
        raise

@when('I list all available books')
def step_impl(context):
    try:
        context.books = context.api_client.list_books()
        logging.info(f"Retrieved {len(context.books)} books")
    except Exception as e:
        logging.error(f"Failed to list books: {e}")
        raise

@when('I reserve two books')
def step_impl(context):
    try:
        # Select two books to reserve 
        isbns_to_reserve = [book['isbn'] for book in context.books[:2]]
        context.api_client.reserve_books(context.user_id, context.auth_token, isbns_to_reserve)
        logging.info(f"Reserved books with ISBNs: {isbns_to_reserve}")
    except Exception as e:
        logging.error(f"Failed to reserve books: {e}")
        raise

@then('I should see the reserved books in the user details')
def step_impl(context):
    try:
        user_details = context.api_client.get_user_details(context.user_id, context.auth_token)
        reserved_books = [book['isbn'] for book in user_details['books']]
        assert len(reserved_books) == 2, f"Expected 2 reserved books, but found {len(reserved_books)}"
        logging.info(f"Verified reserved books: {reserved_books}")
    except Exception as e:
        logging.error(f"Failed to verify reserved books: {e}")
        raise