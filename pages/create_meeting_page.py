from selenium.webdriver.common.by import By
import time

class CreateMeetingBookingPage:
    def __init__(self, driver):
        self.driver = driver


    # Locators
    URL = "https://app.hubspot.com/signup-hubspot/sales?utm_medium=virality&utm_campaign=hubspot-meetings-embedded-virality&step=landing_page"
    ACCEPT_COOKIES_BTN = (By.ID, "hs-eu-confirmation-button")
    EMAIL_FIELD = (By.ID, "FormControl1")
    VERIFY_EMAIL_BTN = (By.XPATH, "//button[.//i18n-string[text()='Verify email']]")
    MANAGE_COOKIES_LINK = (By.LINK_TEXT, "Manage Cookies")
    ACCEPT_ALL_COOKIES_BTN = (By.ID, "hs-modal-accept-all")


    # Create your own meeting booking page
    def open_page(self):
        self.driver.get(self.URL)
        print("Create your own meeting booking Page is opened")
        time.sleep(10)
        print("")
    

    # Accept initial cookies
    def accept_initial_cookies(self):
        accept_btn = self.driver.find_element(*self.ACCEPT_COOKIES_BTN)
        accept_btn.click()
        print("Cookies accepted.")
        time.sleep(10)
        print("")

    
    # Enter email
    def enter_email(self, email_text):
        email_input = self.driver.find_element(*self.EMAIL_FIELD)
        email_input.send_keys(email_text)
        print("Entered email is:", email_input.get_attribute("value"))
        time.sleep(4)
        print("")

    
    # Click verify email
    def click_verify_email(self):
        verify_btn = self.driver.find_element(*self.VERIFY_EMAIL_BTN)
        verify_btn.click()
        print("Verify email button is clicked")
        time.sleep(10)
        print("")

    
    # Manage cookies
    def manage_cookies(self):
        print("Manage Cookies")
        manage_btn = self.driver.find_element(*self.MANAGE_COOKIES_LINK)
        manage_btn.click()
        print("Manage cookies button is clicked")
        time.sleep(10)
        print("")

    
    # Accept all cookies
    def accept_all_cookies(self):
        accept_all_btn = self.driver.find_element(*self.ACCEPT_ALL_COOKIES_BTN)
        accept_all_btn.click()
        print("All cookies accepted.")
        time.sleep(10)
        print("")
