from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class signup:
    def __init__(self, driver):
        self.driver = driver

    # locators 
    USERNAME = (By.ID, "username")
    LOGIN_BUTTON = (By.ID, "loginBtn")    
    SIGN_UP = (By.LINK_TEXT, "sign up")
    SIGN_UP_EMAIL = (By.XPATH, "//input[@id='FormControl1'][@name='EMAIL']")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "button[data-selenium='LANDING_PAGE_button']")
    COOKIE = (By.ID, "hs-eu-confirmation-button")

    
    print("---- Login and Sign up page ----")
    # signup form
    def username(self, user_name_input, signup_email_input):
        username = self.driver.find_element(*signup.USERNAME)
        username.send_keys(user_name_input)
        print("Username entered")
        time.sleep(2)

        login_button = self.driver.find_element(*signup.LOGIN_BUTTON)
        self.driver.execute_script("arguments[0].click();", login_button)
        print("Login button clicked")
        time.sleep(8)

        signup_page = self.driver.find_element(*signup.SIGN_UP)
        self.driver.execute_script("arguments[0].click();", signup_page)
        print("Sign up link clicked")
        time.sleep(5)
        print("")


        print("---- Sign up form ----")
        print("Sign up page opened")
        signup_email = self.driver.find_element(*signup.SIGN_UP_EMAIL)
        self.driver.execute_script("arguments[0].scrollIntoView();", signup_email)
        time.sleep(2)
        signup_email.send_keys(signup_email_input)
        print("Sign up email entered")
        time.sleep(5)


        signup_button = self.driver.find_element(*signup.SIGN_UP_BUTTON)
        self.driver.execute_script("arguments[0].click();", signup_button)
        print("Sign up button clicked")
        time.sleep(5)


        if "Check your email" in self.driver.page_source:
            print("Sign up successful We’ve sent your verification link to you mail text present")
        else:
            print("Sign up failed")

    
    # cookies
    def cookie_accept(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.COOKIE))
        cookie = self.driver.find_element(*self.COOKIE)
        cookie.click()    
        print("Cookies accepted")
        time.sleep(1)

