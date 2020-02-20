import unittest
import time
import sys
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_support.pages import MainPageLocators, MainPage, SidebarAny



class TestSidebarLinks(unittest.TestCase):
    """ Testing if all sidebar links are functional """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mcswiss-web-stage.web.app/")
        self.driver.set_window_size(1920, 1177)
        self.wait = WebDriverWait(self.driver, 100)

    def test_sidebar_links(self):
        sidebar = MainPage(self.driver)

        sidebar.wait_for_element(10, SidebarAny.SIDEBAR_ONE)
        sidebar.click_sidebar_one()
        sidebar.click_sidebar_two()
        sidebar.click_sidebar_three()
        sidebar.click_sidebar_four()
        sidebar.click_sidebar_five()
        sidebar.click_sidebar_six()

    def teardown_method(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()