from selenium.webdriver.common.by import By
from pesto_assessment.Automation_Testscripts.Utility import BaseClass


class SearchPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.ID, "search_input")
        self.search_button = (By.ID, "search_button")
        self.product_list = (By.CLASS_NAME, "product")

    def perform_empty_search(self):
        # Assuming there is a search bar with an "Search" button
        self.driver.find_element(*self.search_button).click()

    def get_product_list(self):
        # Assuming products are displayed in a container with the class "product"
        return self.baseclass.verifylinkpresence(self.product_list)
