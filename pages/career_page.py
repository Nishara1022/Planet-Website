from selenium.webdriver.common.by import By
import time


class Career():
    def __init__(self, driver):
        self.driver = driver

    # locators 
    COOKIES = (By.ID, "cookie_action_close_header")    
    QA = (By.XPATH, "//a[@href='/careers/regular-automation-qa-engineer/']")
    NAME = (By.XPATH, "//input[@name='your-name']")
    EMAIL = (By.XPATH, "//input[@name='your-email']")
    SUBJECT = (By.XPATH, "//input[@name='your-subject']")
    PHONE = (By.XPATH, "//input[@placeholder='Phone (optional)']")
    MESAGE = (By.XPATH, "//textarea[@placeholder='Your message (optional)']")
    RESUME = (By.XPATH, "//input[@name='file-282']")
    TERMS = (By.XPATH, "//input[@id='terms']")
    APPLY = (By.XPATH, "//input[@value='Apply']")


    print("---- Career page ----")
    # title 
    def title(self):
        title = self.driver.find_element(By.TAG_NAME, "h1")
        print(title.text)            
        print("")
        
    # accept cookies
    def cookies(self):
        cookies = self.driver.find_element(*Career.COOKIES)
        time.sleep(10)
        cookies.click()
        print("Cookies accepted")
        time.sleep(1)
        print("")
    
    # click QA 
    def qa(self):
        self.driver.find_element(*Career.QA).click()
        print("Regular Automation QA Engineer button clicked")
        time.sleep(1)
        print("")
    
    # fill Career form
    def fill_form(self, name, email, subject, phone, mesage, resume):
        print("---- Career form ----")
        name_input = self.driver.find_element(*Career.NAME)
        self.driver.execute_script("arguments[0].scrollIntoView();", name_input)
        name_input.send_keys(name)
        print(name_input.get_attribute("value"))
        time.sleep(1)
        
        email_input = self.driver.find_element(*Career.EMAIL)
        email_input.send_keys(email)
        print(email_input.get_attribute("value"))
        time.sleep(1)

        subject_input = self.driver.find_element(*Career.SUBJECT)
        subject_input.send_keys(subject)
        print(subject_input.get_attribute("value"))
        time.sleep(1)
        
        phone_input = self.driver.find_element(*Career.PHONE)
        phone_input.send_keys(phone)
        print(phone_input.get_attribute("value"))
        time.sleep(1)

        mesage_input = self.driver.find_element(*Career.MESAGE)
        mesage_input.send_keys(mesage)
        print(mesage_input.get_attribute("value"))
        time.sleep(1)

        resume_input = self.driver.find_element(*Career.RESUME)
        resume_input.send_keys(resume)
        print(resume_input.get_attribute("value"))
        time.sleep(10)

        self.driver.find_element(*Career.TERMS).click()
        time.sleep(5)
        print("Terms accepted")

        self.driver.find_element(*Career.APPLY).click()
        time.sleep(10)
        print("Apply button clicked")
        

        print("Form filled")
        time.sleep(5)
        print("")


        # test "Thank you for your message. It has been sent."
        if "Thank you for your message. It has been sent." in self.driver.page_source:
            print("Message sent successfully. \n Thank you for your message. It has been sent. message appeared on the page")
        else:
            print("Message not sent")

      
