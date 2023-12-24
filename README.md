# Pesto Assessment Automation Testscripts

This project contains automated test scripts using Pytest, Selenium, and the Page Object Model for the Pesto Assessment. The tests cover scenarios such as empty product searches and user registrations. Test data is read from Excel files, and configurations can be customized through command-line options.

## Project Structure

- `conftest.py`: Contains Pytest fixtures, configuration settings, and functions for reading test data.
- `PageObject/SearchPage.py`: Page Object for the product search page.
- `PageObject/RegistrationPage.py`: Page Object for the user registration page.
- `Utility/BaseClass.py`: Contains a base class for common utility functions.
- `Utility/testlogger.py`: Contains a utility for logging test information.
- `Test_scripts/test_empty_search.py`: Pytest test case for an empty product search.
- `Test_scripts/test_user_registration.py`: Pytest test case for user registration.
- `test_data.xlsx`: Excel file containing test data for the empty product search.
- `Test_datas.xlsx`: Excel file containing test data for user registration.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/pesto-assessment-automation.git
cd pesto-assessment-automation

2. Install the required dependencies:

pip install -r requirements.txt

3.You can run tests by executing the following command:

pytest

4. Customizing Tests

You can customize the tests by adjusting the Page Objects, test cases, and configurations in the conftest.py file and other relevant files.

5. Logging

Test information is logged using the utility provided in Utility/testlogger.py.