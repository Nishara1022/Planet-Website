from selenium.webdriver.common.by import By
import time
# webdriver wait


class Home:   
        def __init__(self, driver):
         self.driver = driver


        COOKIE =  (By.ID, "cookie_action_close_header")
        NAME = (By.XPATH, "//input[@placeholder='Name']")
        EMAIL = (By.XPATH, "//input[@placeholder='Email']")
        MESSAGE = (By.XPATH, "//textarea[@placeholder='Message']")
        TERMS_CHECKBOX = (By.ID, "terms")
        SEND_BUTTON = (By.XPATH, "//input[@value='Send']")
        
        
        print("---- Contact us page ----")
        # accept cookies
        def cookies(self):
            cookies = self.driver.find_element(*Home.COOKIE)
            cookies.click()
            print("Cookies accepted")
            time.sleep(1)
            print("") 


        def title (self):
            title = self.driver.find_element(By.TAG_NAME, "h1")
            print("title: is ", title.text)            
            print("")

        
        # contact us form 
        def contact_us_form(self, name_input, email_input, message_input):
            print("---- Contact us form ----")

            name = self.driver.find_element(*Home.NAME)
            self.driver.execute_script("arguments[0].scrollIntoView();", name)
            name.send_keys(name_input)
            print(name.get_attribute("value"))
            time.sleep(1)

            email = self.driver.find_element(*Home.EMAIL)
            email.send_keys(email_input)
            print(email.get_attribute("value"))
            time.sleep(1)

            message = self.driver.find_element(*Home.MESSAGE)
            message.send_keys(message_input)
            print(message.get_attribute("value"))
            time.sleep(1)

            terms = self.driver.find_element(*Home.TERMS_CHECKBOX)
            terms.click()
            print("Terms accepted")
            time.sleep(10)

            send = self.driver.find_element(*Home.SEND_BUTTON)
            send.click()
            time.sleep(10)
            print("Send button clicked")
            print("Email sent")
            time.sleep(10)

        
            if "Thank you for your message. It has been sent." in self.driver.page_source:
                print("Email sent successfully. Thank you for your message. It has been sent. message displayed")
            else:
                print("Email sent message not displayed")

            