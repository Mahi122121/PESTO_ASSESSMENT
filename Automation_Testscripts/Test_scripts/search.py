import pytest
from selenium.common.exceptions import TimeoutException
from pesto_assessment.Automation_Testscripts.PageObject.SearchPage import SearchPage
from pesto_assessment.Automation_Testscripts.Test_scripts.conftest import read_test_data


@pytest.mark.parametrize("search_query, expected_result", read_test_data("test_data.xlsx", "Empty_search_test_data"))
def test_empty_product_search(browser, search_query, expected_result):
    search_page = SearchPage(browser)

    # Navigate to the search page
    browser.get("URL_TO_YOUR_ECOMMERCE_WEBSITE/search")

    # Perform a search with the provided query
    search_page.perform_search(search_query)

    try:
        # Verify the result based on the expected outcome
        if expected_result.lower() == "success":
            product_list = search_page.get_product_list()
            assert len(product_list) > 0
        elif expected_result.lower() == "failure":
            # You can add additional verification based on failure criteria if needed
            pass
        else:
            pytest.fail(f"Invalid expected result: {expected_result}")

    except TimeoutException:
        # Handle the case where the product list does not appear within the expected time
        pytest.fail("Product list did not appear within the expected time.")