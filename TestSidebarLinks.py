import unittest
import time
import sys
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_support.pages import MainPageLocators, MainPage, SidebarAny, Sidebar



class TestSidebarLinks(unittest.TestCase):
    """ Testing if all sidebar links (even subcategories) are functional """

    def setUp(self):
    
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get("https://mcswiss-web-stage.web.app/")
        self.driver.set_window_size(1920, 1177)
        self.wait = WebDriverWait(self.driver, 100)

    def test_sidebar_links(self):
        sidebar = MainPage(self.driver)

        sidebar.wait_for_element(10, SidebarAny.SIDEBAR_ONE)

        # SIDEBAR_LIST is in locators.py
        for item in Sidebar.SIDEBAR_LIST:
            current_item = self.driver.find_element(By.XPATH, item)
            current_item.click()
        else:
            print("---- Test result: All links in sidebar are working ----")
    

    def teardown_method(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)