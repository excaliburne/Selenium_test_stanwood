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
        category.click_category_non_food()

        item = Items(self.driver)
        item.wait_for_element(30, ItemInCategory.FIRST_ITEM)
        item.click_first_item()

        print("Test successful! Item is present on page")
  
    def teardown_method(self, method):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()