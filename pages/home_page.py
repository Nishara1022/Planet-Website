from selenium.webdriver.common.by import By
import time
# webdriver wait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Home:   
        def __init__(self, driver):
         self.driver = driver


        COOKIE =  (By.ID, "cookie_action_close_header")
        LOGO = (By.ID, "logo-link")
        HEADER = (By.ID,"menu")
        HEADER_LINKS = (By.TAG_NAME, "a")
        CONTACT = (By.XPATH, "//a[@onclick='scrollToContactUs()']")
        CONTENT = (By.ID, "page-content")
        CONTENT_tags = (By.TAG_NAME, "h3")
        TEST_A_B_CONTENT = (By.ID, "tech-overview")
        TEST_A_B_CONTENT_H3 = (By.TAG_NAME, "h3")
        TEST_A_B_CONTENT_P = (By.TAG_NAME, "p")
        HOW_CAN_WE_HELP = (By.ID, "how_we_can_help_section")
        HOW_CAN_WE_HELP_H4 = (By.TAG_NAME, "h4")
        HOW_CAN_WE_HELP_P = (By.TAG_NAME, "p")  
        RIGHT_SETUP = (By.ID, "right-set-up")
        FIRST_CONTACT = (By.XPATH, "//a[@onclick='scrollToContactUs()']")
        READFULL_STORY = (By.XPATH, "//a[@href='/transforming-testing-efficiency-a-test-automation-success-story/']")
        DOWNLOAD = (By.XPATH, "//a[@href='/wp-content/uploads/2025/03/success_story.pdf']")
        READFULL_ARTICLE = (By.XPATH, "//a[normalize-space()='Read Full Article']")
        WEB_AUTOMATION = (By.LINK_TEXT, "Web Automation")
        DESKTOP_AUTOMATION = (By.LINK_TEXT, "Desktop Automation")
        API_AUTOMATION = (By.LINK_TEXT, "API Automation")
        MOBILE_AUTOMATION = (By.LINK_TEXT, "Mobile Automation")
        PRIVATE_TRAINING = (By.LINK_TEXT, "Private Trainings")
        START_THE_TEST = (By.XPATH, "//div[contains(@class,'text-center')]")
        IFRAME = (By.XPATH, "//iframe[@title='Self-Evaluation Quiz']")
        YES_BUTTON = (By.XPATH, "//div[text()='Yes']")
        OK_BUTTON = (By.XPATH, "//button[.//span[text()='OK']]")
        
        BOOKA_MEETING = (By.XPATH, "//h2[text()='Book a Meeting']")
        IFRAME_BOOK_MEETING = (By.XPATH, "//iframe[contains(@src, 'meetings.hubspot.com')]")
        CALENDER = (By.XPATH, "//button[@data-test-id='available-date']")
        DATE = (By.XPATH, "//button[@data-test-id='available-date']//span[text()='28']")
        MINUTES = (By.XPATH, "//button[@data-button-use='view-group']//span[text()='30 mins']")
        TIME_BUTTON = (By.XPATH, "//span[text()='12:15 am']/ancestor::div[@role='checkbox']")
        
        IFRAME_BOOK_MEETING_FORM = (By.XPATH, "//iframe[contains(@src, 'meetings.hubspot.com')]")
        NAME = (By.XPATH, "//input[@data-test-id='confirm-firstName-field']")
        LAST_NAME = (By.ID, "FormControl10")
        EMAIL = (By.ID, "FormControl12")
        DEMO_REQUEST_BUTTON = (By.XPATH, "//button[contains(@class, 'meetings-submit')]")

        FOOTER = (By.ID, "footer")
        FOOTER_LINKS = (By.CSS_SELECTOR, "#footer a")
        SOCIAL_LINKS = (By.CSS_SELECTOR, ".social-links a")

        
        print("---- Home Page ----")
        # accept cookies
        def cookies(self):
            cookies = self.driver.find_element(*Home.COOKIE)
            cookies.click()
            print("Cookies accepted")
            time.sleep(1)
            print("")  

        
        # click logo
        def logo (self):
            logo = self.driver.find_element(*Home.LOGO)
            logo.click()
            print("Logo clicked")
            time.sleep(1)
            print("")    


        # header section
        def header(self):
            print("---- Header Links ----")

            header = self.driver.find_element(*Home.HEADER)
            header_links = header.find_elements(By.TAG_NAME, "a")

            link_data = []
            for link in header_links:
                href = link.get_attribute("href")
                text = link.text.strip()

                if href and "http" in href:  # Ignore empty/JS links
                    link_data.append((text, href))

            for text, href in link_data:
                try:
                    self.driver.get(href)
                    print(f"Link Text: {text}")
                    print("Current URL:", self.driver.current_url)
                    time.sleep(2)
                except Exception as e:
                    print(f"Failed to open {href}: {e}")
            print("All header links tested.")

        
        # contact button
        def contact (self):
            print("Contact")

            contact = self.driver.find_element(*Home.CONTACT)  
            contact.click()
            time.sleep(2)
            print("contact clicked and closed")
            self.driver.back()
            time.sleep(2)


        def back_to_home (self):
            self.driver.get("https://www.automatetheplanet.com/")
            print("Back to home clicked")  
            time.sleep(8)
            print("")  

        
        # first contact button
        def first_contact(self):
            first_contact = self.driver.find_element(*Home.FIRST_CONTACT)
            first_contact.click()
            print("First contact button clicked")
            time.sleep(1)
               

        # readfull story button
        def readfull_story(self):
            readfull_story = self.driver.find_element(*Home.READFULL_STORY)
            readfull_story.click()
            print("Readfull story button clicked")
            time.sleep(1)
            

        # download button
        def download(self):
            download = self.driver.find_element(*Home.DOWNLOAD)
            download.click()
            print("Download button clicked")
            time.sleep(10)
            print("Download completed")
                      

        # read full article button
        def read_full_article(self):
            full_article = self.driver.find_element(*Home.READFULL_ARTICLE)
            full_article.click()
            print("Full article button clicked")
            time.sleep(1)
              

        # Web Automation button
        def web_automation(self):
            web_automation = self.driver.find_element(*Home.WEB_AUTOMATION)
            web_automation.click()
            print("Web automation button clicked")
            time.sleep(1)

        
        # Desktop Automation button
        def desktop_automation(self):
            desktop_automation = self.driver.find_element(*Home.DESKTOP_AUTOMATION)
            desktop_automation.click()
            print("Desktop automation button clicked :")
            time.sleep(1)

        
        # API Automation button
        def api_automation(self):
            api_automation = self.driver.find_element(*Home.API_AUTOMATION)
            api_automation.click()
            print("API automation button clicked")
            time.sleep(1)


        def mobile_automation(self):
            mobile_automation = self.driver.find_element(*Home.MOBILE_AUTOMATION)
            mobile_automation.click()
            print("Mobile automation button clicked")
            time.sleep(1)


        def private_training(self):
            private_training = self.driver.find_element(*Home.PRIVATE_TRAINING)
            private_training.click()
            print("Private training button clicked")
            time.sleep(1)
               

        
        # start the test section
        def start_the_test_section(self):
            print("Start the test section")
            start_the_test = self.driver.find_element(*Home.START_THE_TEST)
            self.driver.execute_script("arguments[0].click();", start_the_test)
            print("Start the test button clicked")
            time.sleep(3)


            iframe = WebDriverWait(self.driver, 10)
            iframe = iframe.until(EC.presence_of_element_located((Home.IFRAME)))
            self.driver.switch_to.frame(iframe)
            print("Iframe opened")
            time.sleep(2)


            YES_BUTTON = (By.XPATH, "//div[text()='Yes']")
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(YES_BUTTON)).click()
            print("Yes button clicked")
            time.sleep(2)

        
            # close iframe
            self.driver.switch_to.default_content()
            print("Iframe closed")
            time.sleep(2)

            

        # book a meeting section
        def book_a_meeting_section(self):
            print("Book a meeting section")
            # Scroll to "Book a Meeting" section
            book_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(Home.BOOKA_MEETING)
            )
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", book_section)
            time.sleep(2)
            print("Scrolled to 'Book a Meeting' section")

            # Wait for iframe and switch to it
            iframe = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(Home.IFRAME_BOOK_MEETING)
            )
            self.driver.switch_to.frame(iframe)
            print("Switched to iframe")

            # Wait until calendar is visible
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(Home.CALENDER)
            )
            print("Calendar is loaded")

            # Click the date (e.g., 9th)
            date_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Home.DATE)
            )
            self.driver.execute_script("arguments[0].click();", date_btn)
            print("Date clicked")
            time.sleep(3)

            # Click "30 mins"
            minutes_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Home.MINUTES)
            )
            self.driver.execute_script("arguments[0].click();", minutes_btn)
            print("30 mins clicked")
            time.sleep(3)

            # Click time button 
            time_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Home.TIME_BUTTON)
            )
            self.driver.execute_script("arguments[0].click();", time_btn)
            print("Time button clicked")
            time.sleep(3)

            # Optionally switch back if needed
            self.driver.switch_to.default_content()
            time.sleep(10)         
            print("Iframe closed")
            time.sleep(2)
            print("Successfully clicked 'Book a Meeting' button")
            print("open page ", self.driver.current_url)

    

        # Content
        def content (self):
            print("Content")

            content = self.driver.find_element(*Home.CONTENT)  
            content_links = content.find_elements(*Home.CONTENT_tags) 
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(content_links[0]))
            for links in content_links:
                print(links.text)
                time.sleep(2)
            print("")  


        def TAB_content_h3 (self):
            print("TAB content h3")

            tab_content = self.driver.find_element(*Home.TEST_A_B_CONTENT)  
            tab_content_h3 = tab_content.find_elements(By.TAG_NAME,"h3")
            for links in tab_content_h3:
                print(links.text)
                time.sleep(2)
            print("")
   
    
        def TAB_content_p (self):
            print("TAB content p")

            tab_content = self.driver.find_element(*Home.TEST_A_B_CONTENT)  
            tab_content_p = tab_content.find_elements(*Home.TEST_A_B_CONTENT_P) 
            for links in tab_content_p:
                print(links.text)
                time.sleep(2)
            print("")


        def how_can_we_help_h4(self):
            print("How can we help h4")
            how_can_we_help = self.driver.find_element(*Home.HOW_CAN_WE_HELP)
            tags = how_can_we_help.find_elements(*Home.HOW_CAN_WE_HELP_H4)
            for tag in tags:
                print(tag.text)  
            print("")


        def how_can_we_help_p(self):
            print("How can we help p")
            how_can_we_help = self.driver.find_element(*Home.HOW_CAN_WE_HELP)
            tags = how_can_we_help.find_elements(*Home.HOW_CAN_WE_HELP_P)
            for tag in tags:
                print(tag.text)
            print("")    


        def Right_SetUph4(self):
            print("Right SetUp h4")

            right_set_up = self.driver.find_element(*Home.RIGHT_SETUP)
            tags = right_set_up.find_elements(*Home.TEST_A_B_CONTENT_H3)
            for tag in tags:
                print(tag.text)
            print("")


        def Right_SetUpP(self):
            print("Right SetUp p")
            right_set_up = self.driver.find_element(*Home.RIGHT_SETUP)
            tags = right_set_up.find_elements(*Home.TEST_A_B_CONTENT_P)
            for tag in tags:
                print(tag.text)
            print("")             



