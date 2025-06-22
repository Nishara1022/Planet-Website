from selenium.webdriver.common.by import By
import time

class WebAutomation:   
        def __init__(self, driver):
         self.driver = driver
            

        COOKIE = (By.ID, "cookie_action_close_header")
        JAVA_TAB = (By.XPATH, "//div[contains(text(),'Java')]")
        CSHARP_TAB = (By.XPATH, "//div[contains(text(),'C#')]")
        JAVASCRIPT_TAB = (By.XPATH, "//div[contains(text(),' Javascript')]")
        KOTLIN_TAB = (By.XPATH, "//div[contains(text(),'Kotlin')]")

        SENDUS_AN_EMAIL = (By.XPATH, "//h3[normalize-space()='Send Us an Email']")
        NAME_INPUT = (By.NAME, "yourname")
        EMAIL_INPUT = (By.NAME, "email")
        MESSAGE_INPUT = (By.NAME, "message")
        TERMS_LINK = (By.XPATH, "//a[@href='https://www.automatetheplanet.com/privacy-policy/']")
        SEND_BUTTON = (By.XPATH, "//input[@value='Send']")
        EMAIL_HEADER = (By.XPATH, "//h3[normalize-space()='Send Us an Email']")

        
        print("---- Web Automation page ----")
        # accept cookies
        def cookie_accept(self):
            cookie = self.driver.find_element(*WebAutomation.COOKIE)
            cookie.click()
            print("Cookie accepted")
            time.sleep(1)
            print("")

        
        # tabs
        def tabs(self):
            print("---- Tabs ----")

            java = self.driver.find_element(*WebAutomation.JAVA_TAB)
            java.click()
            print("Java tab clicked")

            csharp = self.driver.find_element(*WebAutomation.CSHARP_TAB)
            csharp.click()
            print("C# tab clicked")
            
            javascript = self.driver.find_element(*WebAutomation.JAVASCRIPT_TAB)
            javascript.click()
            print("Javascript tab clicked")

            kotlin = self.driver.find_element(*WebAutomation.KOTLIN_TAB)
            kotlin.click()
            print("Kotlin tab clicked")
            print("")


       
        # book a meeting form
        def book_a_meeting_form(self, name_input, email_input, message_input):
            print("---- Book a meeting form ----")
            book_a_meeting = self.driver.find_element(*WebAutomation.SENDUS_AN_EMAIL)
            self.driver.execute_script("arguments[0].scrollIntoView();", book_a_meeting)
            self.driver.execute_script("arguments[0].click();", book_a_meeting)
            print("Send us an email clicked")

            name = self.driver.find_element(*WebAutomation.NAME_INPUT)
            name.send_keys(name_input)
    
            email = self.driver.find_element(*WebAutomation.EMAIL_INPUT)
            email.send_keys(email_input)

            message = self.driver.find_element(*WebAutomation.MESSAGE_INPUT)
            message.send_keys(message_input)

            terms = self.driver.find_element(*WebAutomation.TERMS_LINK)
            terms.click()
            print("Terms accepted")


            send = self.driver.find_element(*WebAutomation.SEND_BUTTON)
            send.click()
            print("Send button clicked")
        
            header = self.driver.find_element(*WebAutomation.EMAIL_HEADER)
            print(header.text)
            print("Email sent")

            return name, email, message
