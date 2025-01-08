import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ApiClient:
    def __init__(self, base_url="https://demoqa.com"):
        self.base_url = base_url

    def _make_request(self, method, endpoint, json=None, headers=None):
        url = self.base_url + endpoint
        
        # Initialize default headers if none provided
        if headers is None:
            headers = {}
        
        # Always set Content-Type for POST and PUT requests
        if method.upper() in ['POST', 'PUT']:
            headers['Content-Type'] = 'application/json'
            headers['Accept'] = 'application/json'
            
        try:
            logging.info(f"Making {method} request to {url}")
            logging.info(f"Headers: {headers}")
            logging.info(f"Payload: {json}")
            
            response = requests.request(method, url, json=json, headers=headers)
            logging.info(f"Response status: {response.status_code}")
            logging.info(f"Response body: {response.text}")
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {e}")
            logging.error(f"Response content: {getattr(e.response, 'text', 'No response content')}")
            raise

    def create_user(self, username, password):
        endpoint = "/Account/v1/User"
        data = {
            "userName": username,
            "password": password
        }
        return self._make_request("POST", endpoint, json=data)

    def generate_token(self, username, password):
        endpoint = "/Account/v1/GenerateToken"
        data = {
            "userName": username,
            "password": password
        }
        response = self._make_request("POST", endpoint, json=data)
        return response["token"]

    def list_books(self):
        endpoint = "/BookStore/v1/Books"
        response = self._make_request("GET", endpoint)
        return response["books"]

    def reserve_books(self, user_id, auth_token, isbns):
        endpoint = "/BookStore/v1/Books"
        headers = {
            "Authorization": f"Bearer {auth_token}"
        }
        for isbn in isbns:
            data = {
                "userId": user_id,
                "collectionOfIsbns": [{"isbn": isbn}]
            }
            self._make_request("POST", endpoint, json=data, headers=headers)

    def get_user_details(self, user_id, auth_token):
        endpoint = f"/Account/v1/User/{user_id}"
        headers = {
            "Authorization": f"Bearer {auth_token}"
        }
        return self._make_request("GET", endpoint, headers=headers)