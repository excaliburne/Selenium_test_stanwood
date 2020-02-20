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
        
        # SIDEBAR_LIST is in loctors.py
        for item in SidebarAny.SIDEBAR_LIST:
            current_item = self.driver.find_element(By.XPATH, item)
            print("Link is working")
            current_item.click()
        else:
            print("---- Test result: All links in sidebar are working ----")
            


        """
        Following code is another implementation of the code above. A for loop is just more concise
        but you can be more specific with the code below. Ex: clicking element in any order

        sidebar.wait_for_element(10, SidebarAny.SIDEBAR_ONE)
        sidebar.click_sidebar_one()
        sidebar.click_sidebar_two()
        sidebar.click_sidebar_three()
        sidebar.click_sidebar_four()
        sidebar.click_sidebar_five()
        sidebar.click_sidebar_six()
        """

    

    def teardown_method(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)