import unittest
import time
import sys
import json
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from test_support.pages import MainPageLocators, MainPage, Sidebar, ItemInCategory, Items

class TestItemInCategory(unittest.TestCase):
    """ Test if item is on page after clicking on category """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mcswiss-web-stage.web.app/")
        self.driver.set_window_size(1920, 1177)
        self.wait = WebDriverWait(self.driver, 100)

    def test_item_in_category(self):
        category = MainPage(self.driver)

        # Click the "Nonfood" category in sidebar
        category.click_category_non_food()

        # Wait for element to appear and click on first item on list
        item = Items(self.driver)
        item.wait_for_element(30, ItemInCategory.FIRST_ITEM)
        assert item.is_element_present(*ItemInCategory.FIRST_ITEM)
        item.click_first_item()

        self.driver.back()

        # driver.back() is going to previous page and now selenium clicks on second item if present
        item.wait_for_element(30, ItemInCategory.SECOND_ITEM)
        assert item.is_element_present(*ItemInCategory.SECOND_ITEM)
        item.click_second_item()

        print("---- Test result: Test successful! Items are present on page ----")
  
    def teardown_method(self, method):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)