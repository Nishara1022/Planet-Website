from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# select
from selenium.webdriver.support.ui import Select

class DemoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    
   # locators 
    USERNAME = (By.ID, "username")
    SIGN_UP = (By.ID, "loginBtn")
    DEMO_BUTTON = (By.XPATH, "//a[@data-test-id='demo-button']")
    COOKIE = (By.ID, "hs-eu-confirmation-button") #hs-eu-confirmation-button
    IFRAME = (By.CSS_SELECTOR, "iframe[title*='HubSpot']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Close']")
    FIRSTNAME_INPUT = (By.NAME, "firstname")
    LASTNAME_INPUT = (By.NAME, "lastname")
    EMAIL_INPUT = (By.NAME, "email")
    PHONE_INPUT = (By.NAME, "phone")
    COMPANY_INPUT = (By.NAME, "company")
    WEBSITE_INPUT = (By.NAME, "website")
    EMPLOYEES_DROPDOWN = (By.ID, "employees__c-95c7a26e-eb03-4da7-bb69-4ca3c029983b")
    COUNTRY_DROPDOWN = (By.ID, "country_dropdown-95c7a26e-eb03-4da7-bb69-4ca3c029983b")
    GET_DEMO_BUTTON = (By.XPATH, "//input[@type='submit' and @class='hs-button primary large' and @value='Get your free demo']")


    print("---- Demo page ----")
    # accept cookie
    def cookie_accept(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.COOKIE))
        cookie = self.driver.find_element(*self.COOKIE)
        self.driver.execute_script("arguments[0].click();", cookie)
        print("Cookies accepted")
        time.sleep(1)
        print("")


    # username
    def username(self, username_input):
        username = self.driver.find_element(*self.USERNAME)
        username.send_keys(username_input)
        print("Username entered")
        time.sleep(2)
        print("")


    # sign up
    def sign_up(self):
        sign_up = self.driver.find_element(*self.SIGN_UP)
        self.driver.execute_script("arguments[0].click();", sign_up)
        print("Sign up clicked")
        time.sleep(1)
        print("")

    
    # click demo
    def click_demo_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.DEMO_BUTTON))
        demo_btn = self.driver.find_element(*self.DEMO_BUTTON)
        self.driver.execute_script("arguments[0].click();", demo_btn)   
        print("Get a Demo button is clicked")
        time.sleep(15)
        print("")

    
    # close popup
    def close_iframe(self):
        try:
            wait = WebDriverWait(self.driver, 20)

            # Wait for iframe to be present
            iframe = wait.until(EC.presence_of_element_located(self.IFRAME))
            self.driver.switch_to.frame(iframe)

            # Wait for close button to be clickable
            close_button = wait.until(EC.element_to_be_clickable(self.CLOSE_BUTTON))
            close_button.click()
            print("Popup closed successfully.")

            self.driver.switch_to.default_content()

        except Exception as e:
            print("Failed to close popup:", e)
            # Optional: switch back to main content if switched inside try
            try:
                self.driver.switch_to.default_content()
            except Exception:
                pass
            print("")

    
    # fill Demo form
    def fill_demo_form(self, firstname, lastname, email, phone, company, website, employees, country):
        print("---- Demo form ----")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FIRSTNAME_INPUT))
        firstname_input = self.driver.find_element(*self.FIRSTNAME_INPUT)
        firstname_input.clear()
        firstname_input.send_keys(firstname)
        print("Enter first name:", firstname_input.get_attribute("value"))
        time.sleep(2)

        lastname_input = self.driver.find_element(*self.LASTNAME_INPUT)
        lastname_input.send_keys(lastname)
        print("Enter last name:", lastname_input.get_attribute("value"))
        time.sleep(2)

        email_input = self.driver.find_element(*self.EMAIL_INPUT)
        email_input.send_keys(email)
        print("Enter email:", email_input.get_attribute("value"))
        time.sleep(2)

        phone_input = self.driver.find_element(*self.PHONE_INPUT)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", phone_input)
        phone_input.send_keys(phone)
        print("Enter phone:", phone_input.get_attribute("value"))
        time.sleep(2)

        company_input = self.driver.find_element(*self.COMPANY_INPUT)
        company_input.send_keys(company)
        print("Enter company name:", company_input.get_attribute("value"))
        time.sleep(5)

        website_input = self.driver.find_element(*self.WEBSITE_INPUT)
        website_input.send_keys(website)
        print("Enter website:", website_input.get_attribute("value"))
        time.sleep(5)


        employees_dropdown = self.driver.find_element(*self.EMPLOYEES_DROPDOWN)
        employees_select = Select(employees_dropdown)
        employees_select.select_by_visible_text(employees)
        print("Selected employees:", employees)
        time.sleep(2)

        country_dropdown = self.driver.find_element(*self.COUNTRY_DROPDOWN)
        country_select = Select(country_dropdown)
        country_select.select_by_visible_text(country)
        print("Selected country:", country)
        time.sleep(2)


        get_demo = self.wait.until(EC.element_to_be_clickable(self.GET_DEMO_BUTTON))
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", get_demo)
        time.sleep(6)
        self.driver.execute_script("arguments[0].click();", get_demo)
        print("Get your demo button is clicked")
        print("Demo form filled successfully.")
        time.sleep(20)
        print("")

