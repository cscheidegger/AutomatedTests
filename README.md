# QA Automation Exercise

Welcome to my QA automation exercise! This project is a practice-driven exploration into QA automation using tools like Cucumber (BDD for Python). The goal is to enhance my automation skills while ensuring a clear and structured approach to testing.

This repository demonstrates automated testing capabilities for both **API** and **Frontend** scenarios. It is divided into two main parts:

1. **API Automation**: Validates the functionality of a book management API.
2. **Frontend Automation**: Simulates user interactions with a web interface tied to the same API.

---

## **Project Purpose**

The primary purpose of this project is to:
- Automate testing workflows for an API and its frontend counterpart.
- Ensure seamless user experiences through reliable end-to-end tests.
- Practice clean, reusable, and scalable coding practices.

---

## **Key Objectives**

1. Automate end-to-end testing of the API.
2. Simulate realistic user interactions with the web interface.
3. Align backend and frontend functionalities through shared test cases.
4. Highlight debugging strategies for QA automation challenges.

---

## **How to Run the Project**

### **Prerequisites**
Ensure the following are installed on your system:
- **Python 3.10+**
- **pip** (Python package installer)
- **Google Chrome** (for frontend automation)
- **ChromeDriver** (compatible with your Chrome version)

### **Setup Instructions**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/cscheidegger/Automation.git
   cd Automation

2. Set Up a Virtual Environment
python -m venv venv

3. Activate the Virtual Environment
Windows: .\venv\Scripts\activate
Mac/Linux: source venv/bin/activate

4. Install Dependencies
   pip install -r requirements.txt

5. Verify Installation
   pip list


Running Tests
Part 1: API Automation

To validate the API functionality:

1. Navigate to the api_automation directory:
cd api_automation

2. Run Behave tests:
behave features

Key Points for API Automation:
I created a unique username, to be generated automatically
If issues occur:
Verify that the API server is running and accessible.
Confirm that the generated username is unique.
Check the Swagger documentation to ensure endpoint functionality aligns with expectations.
https://demoqa.com/swagger/#/Account/AccountV1UserByUserIdDelete

Running Tests: Frontend Automation

To test the web interface:
1. Navigate to the frontend_automation directory:
cd frontend_automation
2. Run the frontend test suite:
python -m unittest discover -s tests -p "test_*.py"

Key Points for Frontend Automation:
Ensure Google Chrome and ChromeDriver are installed and compatible.  ( I used this tutorial for reference : https://www.youtube.com/watch?v=sdNmNS23_Gs) 

Tests simulate user interactions aligned with API functionality, such as:

Starting and stopping progress bars.

Sorting lists of items interactively.

For debugging:

Use F12 Developer Tools in Chrome to inspect elements and identify the appropriate locators.
Check the console elements using F12 in : https://demoqa.com/

Project Structure
```qa_automation/
├── api_automation/           # API Automation Tests
│   ├── api_client.py         # API Client for interacting with backend endpoints
│   ├── features/             # Behave feature files and step definitions
│   │   ├── api_test.feature  # Gherkin feature file for API tests
│   │   ├── steps/            # Step definitions for Behave tests
│   │       ├── api_steps.py  # Implementation of test steps
│   ├── requirements.txt      # API automation dependencies
│
├── frontend_automation/      # Frontend Automation Tests
│   ├── tests/                # Test scripts for frontend automation
│   │   ├── test_demoqa.py    # Test cases for the web interface
│   ├── requirements.txt      # Frontend automation dependencies
│
├── README.md                 # Project documentation
```
Possible Improvements : 

While building this project, I realized a few areas for growth:

Frontend Automation:
Implement screenshot capture on test failures.
Add more robust error handling for dynamic elements.

API Automation:
Extend tests for edge cases, such as invalid user input or server errors.
Improve API response validation to include schema validation.


Dependencies
API Automation:
behave: For BDD testing.
requests: For making API calls.
Frontend Automation:
selenium: For browser-based UI testing.
unittest: For structuring test cases.

Contribution
If you'd like to improve or extend this project:

Fork the repository.
Create a feature branch.
Submit a pull request with detailed explanations of your changes.

Contact
For any questions or support, feel free to reach out:

* Caio Scheidegger*
* Email: cscheidegger@gmail.com
* LinkedIn: Caio Scheidegger


