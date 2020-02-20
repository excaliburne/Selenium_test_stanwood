from selenium.webdriver.common.by import By

class MainPageLocators():
    """All locators for main & registration page"""

    """ Register and signup link """

    REGISTER_LINK = (By.XPATH, "//span[contains(.,'Registrieren')]")
    SIGNUP_LINK = (By.XPATH, "//a[contains(.,'Anmelden')]")

    """ Registration page """

    REGISTRATION_FIRSTNAME = (By.XPATH, "//input[@id=\'formly_1_input_firstName_0\']")
    REGISTRATION_LASTNAME = (By.XPATH, "//input[@id=\'formly_1_input_lastName_1\']")
    REGISTRATION_PHONE = (By.XPATH, "//input[@id=\'formly_1_phone-input_phone_2\']")
    REGISTRATION_CITY = (By.XPATH, "//input[@id=\'formly_1_input_city_3\']")
    REGISTRATION_ZIP = (By.XPATH, "//input[@id=\'formly_1_input_zip_4\']")
    REGISTRATION_STREET = (By.XPATH, "//input[@id=\'formly_1_input_street_5\']")
    REGISTRATION_CALENDAR_BUTTON = (By.XPATH, "//button/i")

    REGISTRATION_RESIDENCE_DROP = (By.XPATH, "//ng-select[@id=\'formly_1_select-input_residenceCountryCode_7\']/div/span")
    REGISTRATION_ITEM_INSIDE_RESIDENCE_DROP = (By.XPATH, "//ng-dropdown-panel/div/div[2]/div[3]")

    REGISTRATION_NATIONALITY_DROP = (By.CSS_SELECTOR, "#formly_1_select-input_nationalityCountryCode_8 .ng-arrow-wrapper")
    REGISTRATION_ITEM_INSIDE_NATIONALITY_DROP = (By.XPATH, "//div[2]/div[6]")

    REGISTRATION_EMAIL = (By.XPATH, "//input[@id=\'formly_1_input_email_9\']")
    REGISTRATION_PASSWORD = (By.XPATH, "//input[@id=\'formly_2_input_password_0\']")
    REGISTRATION_PASSWORD_CONFIRM = (By.XPATH, "//input[@id=\'formly_2_input_passwordConfirm_1\']")
    REGISTRATION_INPUT_COMPANY = (By.XPATH, "//input[@id=\'formly_2_input_companyName_11\']")
    REGISTRATION_UPLOAD_BUTTON = (By.ID, "formly_2_file_businessLicense_12")

    REGISTRATION_COMPANY_TYPE_DROP = (By.CSS_SELECTOR, "formly-field:nth-of-type(16) > app-formly-wrapper-form-field  app-select-input-field > ng-select[role='listbox'] input[role='combobox']")
    REGISTRATION_ITEM_INSIDE_COMPANY_TYPE = (By.CSS_SELECTOR, "div:nth-of-type(2) > div:nth-of-type(4)")
    
    REGISTRATION_IBAN = (By.XPATH, "//input[@id=\'formly_2_input_iban_18\']")

    REGISTRATION_CHECKBOX = (By.XPATH, "//ngb-modal-window[@role='dialog']/div[@role='document']//app-registration-modal/app-modal/div[@class='modal-body']/div/div[2]/div/formly-form/formly-field[20]/app-formly-wrapper-form-field//app-formly-field-checkbox//input[@type='checkbox']")
    REGISTRATION_REGISTER_BUTTON = (By.XPATH, "//button[2]/span")

    """Successfull registration message"""

    SUCCESSFULL_REGISTRATION = (By.XPATH, "/html/body/app-root/app-toasts/div/app-toast/div/div[1]")

    """Search button """

    SEARCH_BUTTON = (By.XPATH, "//div[2]/button")


class Sidebar():
    """Sidebar locator with names"""

    CATEGORY_BEVERAGE = (By.XPATH, "//a[contains(.,' Getränke')]")
    CATEGORY_FISH = (By.XPATH, "//a[contains(.,' Fisch')]")
    CATEGORY_NONFOOD = (By.XPATH, "//a[contains(.,' NonFood')]")

class SidebarAny():
    """Sidebar locator without any specific names"""

    SIDEBAR_ONE = (By.XPATH, "//nav/ul/div[1]/a")
    SIDEBAR_TWO = (By.XPATH, "//nav/ul/div[2]/a")
    SIDEBAR_THREE = (By.XPATH, "//nav/ul/div[3]/a")
    SIDEBAR_FOUR = (By.XPATH, "//div[4]/a")
    SIDEBAR_FIVE = (By.XPATH, "//div[5]/a")
    SIDEBAR_SIX = (By.XPATH, "//div[6]/a")

    # This is a list of XPATH strings to be able to iterate through them
    SIDEBAR_LIST = ["//nav/ul/div[1]/a", "//nav/ul/div[2]/a", "//nav/ul/div[3]/a", "//div[4]/a", "//div[5]/a", "//div[6]/a"]

class ItemInCategory():
    """After any category has been clicked, following items should appear"""

    FIRST_ITEM = (By.XPATH, "//div[2]/div/div/a") # First item to appear after any category has been clicked. Notes: This is valid for any category and not entitled to this specific one
    SECOND_ITEM = (By.XPATH, "//div[3]/app-product-preview/div/div[2]/div/div/a")
    THIRD_ITEM = (By.XPATH, "//div[4]/app-product-preview/div/div[2]/div/div/a")