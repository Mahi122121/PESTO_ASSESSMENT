import pytest
from pesto_assessment.Automation_Testscripts.PageObject import RegistrationPage
from pesto_assessment.Automation_Testscripts.Test_scripts.conftest import read_test_data
from pesto_assessment.Automation_Testscripts.Utility import BaseClass
from pesto_assessment.Automation_Testscripts.Utility import testlogger


class TestUserReg():

    @pytest.mark.parametrize("username, email, password, confirm_password, expected_message",
                             read_test_data("Test_datas.xlsx", "User_registration_test_data"))
    def test_user_registration(self, browser, username, email, password, confirm_password, expected_message):
        registration_page = RegistrationPage.RegistrationPage(self.driver)
        Logger = testlogger.Testgetlogger()
        try:

            # Fill in user details from test data
            registration_page.fill_registration_form(username, email, password, confirm_password)

            # Click the "Register" button
            registration_page.click_register_button()

            if "successful" in expected_message.lower():
                # Verify successful registration message
                success_message = registration_page.get_success_message()
                assert expected_message in success_message
                Logger.test_log().info("user registration successfull!")

        except:
            # Verify error messages for invalid registration
            error_message = registration_page.get_error_message()
            assert expected_message in error_message
            Logger.test_log().error("User registration Unsuccessfull!")
