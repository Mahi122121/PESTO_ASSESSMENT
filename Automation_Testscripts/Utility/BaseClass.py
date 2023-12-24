import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifylinkpresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def verifybuttonclickable(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()
