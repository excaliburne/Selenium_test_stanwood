import unittest
import time
import sys
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

class TestShoppingCart(unittest.TestCase):
    """ Test shopping cart """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mcswiss-web-stage.web.app/")
        self.driver.set_window_size(1920, 1177)
        self.wait = WebDriverWait(self.driver, 100)


    def teardown_method(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()