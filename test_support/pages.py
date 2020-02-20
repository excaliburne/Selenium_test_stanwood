import random
import string
import sys
from test_support.locators import MainPageLocators, Sidebar, ItemInCategory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    def __init__(self, driver):
        self.driver = driver 
    
    def click_element(self, *locator):
        element = self.driver.find_element(*locator)
        element.click()
    
    def set_text(self, text, *locator):
        element = self.driver.find_element(*locator)
        element.click()
        element.send_keys(text)
    
    def wait_for_element(self, delay, locator):
        WebDriverWait(self.driver, delay).until(EC.visibility_of_element_located(locator))
        
    def is_element_present(self, *locator):
        element = self.driver.find_element(*locator)
        return element 
    
    def return_message_text(self, *locator):
        element = self.driver.find_element(*locator)
        return element.text 

    def return_message_value(self, *locator):
        element = self.driver.find_element(*locator)
        return element.get_attribute('innerHTML') 

    def get_random_email(self):
        email_account = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        domain = 'xcv.com'
        email = email_account + '@' + domain
        return email

class MainPage(BasePage):
    # Home page actions

    def click_register_link(self):
        super(MainPage, self).click_element(*MainPageLocators.REGISTER_LINK)

    def set_first_name(self, text):
        super(MainPage, self).set_text(text, *MainPageLocators.REGISTRATION_FIRSTNAME)

    def set_last_name(self, text):
        super(MainPage, self).set_text(text, *MainPageLocators.REGISTRATION_LASTNAME)
    
    def set_phone(self, text):
        super(MainPage, self).set_text(text, *MainPageLocators.REGISTRATION_PHONE)
    
    def set_city(self, text):
        super(MainPage, self).set_text(text, *MainPageLocators.REGISTRATION_CITY)
    
    def set_zip(self, text):
        super(MainPage, self).set_text(text, *MainPageLocators.REGISTRATION_ZIP)

    def set_street(self, text):
        super(MainPage, self).set_text(text, *MainPageLocators.REGISTRATION_STREET)

    def click_calendar_button(self):
        super(MainPage, self).click_element(*MainPageLocators.REGISTRATION_CALENDAR_BUTTON)
    
    def click_residence_drop(self):
        super(MainPage, self).click_element(*MainPageLocators.REGISTRATION_RESIDENCE_DROP)
    
    def click_residence_drop_inside(self):
        super(MainPage, self).click_element(*MainPageLocators.REGISTRATION_ITEM_INSIDE_RESIDENCE_DROP)
    
    def click_nationality_drop(self):
        super(MainPage, self).click_element(*MainPageLocators.REGISTRATION_NATIONALITY_DROP)
    
    def click_nationality_drop_inside(self):
        super(MainPage, self).click_element(*MainPageLocators.REGISTRATION_ITEM_INSIDE_NATIONALITY_DROP)
    
    def set_email(self, text):
        super(MainPage, self).set_text(text, *MainPageLocators.REGISTRATION_EMAIL)
    
    def set_password(self, text):
        super(MainPage, self).set_text(text, *MainPageLocators.REGISTRATION_PASSWORD)
    
    def set_password_confirm(self, text):
        super(MainPage, self).set_text(text, *MainPageLocators.REGISTRATION_PASSWORD_CONFIRM) 
    
    def set_company_name(self, text):
        super(MainPage, self).set_text(text, *MainPageLocators.REGISTRATION_INPUT_COMPANY)
    
    def upload_photo(self, text):
        super(MainPage, self).set_text(text, *MainPageLocators.REGISTRATION_UPLOAD_BUTTON)
    
    def click_company_type(self):
        super(MainPage, self).click_element(*MainPageLocators.REGISTRATION_COMPANY_TYPE_DROP)
    
    def click_company_type_inside(self):
        super(MainPage, self).click_element(*MainPageLocators.REGISTRATION_ITEM_INSIDE_COMPANY_TYPE)

    def set_iban(self, text):
        super(MainPage, self).set_text(text, *MainPageLocators.REGISTRATION_IBAN)

    def click_register_button(self):
        super(MainPage, self).click_element(*MainPageLocators.REGISTRATION_REGISTER_BUTTON)

    """Sidebar"""

    def click_category_non_food(self):
        super(MainPage, self).click_element(*Sidebar.CATEGORY_NONFOOD)
    
    def click_category_beverage(self):
        super(MainPage, self).click_element(*Sidebar.CATEGORY_BEVERAGE)
    
    def click_category_fish(self):
        super(MainPage, self).click_element(*Sidebar.CATEGORY_FISH)

class Items(BasePage):

    def click_first_item(self):
        super(Items, self).click_element(*ItemInCategory.FIRST_ITEM)

    




