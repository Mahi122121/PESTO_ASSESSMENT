from selenium.webdriver.common.by import By
from pesto_assessment.Automation_Testscripts.Utility import BaseClass


class RegistrationPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.confirm_password_input = (By.ID, "confirm_password")
        self.register_button = (By.ID, "register_button")
        self.success_message = (By.ID, "registration_success_message")
        self.error_message = (By.CLASS_NAME, "error_message")

    def fill_registration_form(self, username, email, password, confirm_password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.confirm_password_input).send_keys(confirm_password)

    def click_register_button(self):
        self.driver.find_element(*self.register_button).click()

    def get_success_message(self):
        return self.baseclass.verifylinkpresence(self.success_message)

    def get_error_message(self, ):
        return self.baseclass.verifylinkpresence(self.error_message)
