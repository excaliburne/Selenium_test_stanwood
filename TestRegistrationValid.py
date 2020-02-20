import unittest
import time
import sys
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from test_support.pages import MainPageLocators, MainPage

class TestRegistration(unittest.TestCase):
    """ Full registration page """

    def setUp(self):
        # Initiate driver, change to Firefox() if necessary
        self.driver = webdriver.Chrome()
        self.driver.get("https://mcswiss-web-stage.web.app/")
        self.driver.set_window_size(1920, 1177)
        self.wait = WebDriverWait(self.driver, 100)
  
    def test_registration(self):

        register = True  # Set to True if you want the test to register an account, leave to False if you want the
                         # test to fill all items but not register an account in the end

        # Setting registration variable to be equal to the MainPage functions in test_support/pages.py
        registration = MainPage(self.driver)

        # Click "register link"
        registration.click_register_link()

        registration.set_first_name("John")
        registration.set_last_name("Smith")
        registration.set_phone("+49 (2343) 5352 5523")
        registration.set_city("Con")
        registration.set_zip("10616")
        registration.set_street("Tedre")
        registration.click_calendar_button()

        # Open calendar, select year and date
        element = self.driver.find_element(By.XPATH, "//button/i")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.XPATH, "//select[2]").click() # Click "year" option in calendar
        dropdown = self.driver.find_element(By.CSS_SELECTOR, ".custom-select:nth-child(2)")
        dropdown.find_element(By.XPATH, "//option[. = '1989']").click() # Choosing year in list
        self.driver.find_element(By.XPATH, "//div[3]/div[5]/div").click() # Choosing date

        # Select residence
        registration.click_residence_drop()
        registration.click_residence_drop_inside()

        # Select nationality
        registration.click_nationality_drop()
        registration.click_nationality_drop_inside()

        # Get a random email and input email
        email = registration.get_random_email()
        registration.set_email(email)

        # Set password and confirm password
        registration.set_password("TestLOGIN300")
        registration.set_password_confirm("TestLOGIN300")

        # Set company name
        registration.set_company_name("MB")

        # uploading photo
        self.driver.find_element(By.ID, "formly_2_file_businessLicense_12").send_keys("/Users/jeremy/Downloads/devolon.png")

        # Select company type
        registration.click_company_type()
        registration.click_company_type_inside()

        # Set Iban number
        registration.set_iban("DE89500105172843131546")

        # checkbox will be checked with Javascript because html-span obscures it so selenium cannot click the box
        elem = self.driver.find_element(By.XPATH, "//ngb-modal-window[@role='dialog']/div[@role='document']//app-registration-modal/app-modal/div[@class='modal-body']/div/div[2]/div/formly-form/formly-field[20]/app-formly-wrapper-form-field//app-formly-field-checkbox//input[@type='checkbox']")
        self.driver.execute_script("arguments[0].click();", elem)

        # This is the logic to register an account or not
        if register == False:
            print("All element filled but did not register. Set 'register' to 'True' if you want the test to register an actual account")
            sys.exit()
        else:
            print("continuing...")

        # Click register button
        registration.click_register_button()
        print("---- Test result: Test successful! Registration is done. ----")

        """ Optional check with assertEquals
        success = registration.return_message_value(*MainPageLocators.SUCCESSFULL_REGISTRATION)
        self.assertEquals(success, 'Danke für Ihre Registrierung', 'Did not register properly')
        """


    def teardown_method(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)