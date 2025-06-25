from selenium.webdriver.common.by import By
import time

class Resources:   
        def __init__(self, driver):
         self.driver = driver


        # locators
        COOKIE = (By.ID, "cookie_action_close_header")
        SEARCH = (By.XPATH, "//input[@type='search']")
        SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
        LEARN_MORE = (By.XPATH, "//a[@class='button push-top-20  push-right-20']")
        AVAILABLE_OPTIONS = (By.XPATH, "//label[@for='collapsible-head']")
        PURCHASE_BOOKS_DE_LINK = (By.XPATH, "//a[text()='Purchase EN Books (DE)']")
        DOWNLOAD_PAPER_BUTTON = (By.XPATH, "//a[text()='Download this papper']")
        NAME_INPUT = (By.NAME, "name")
        EMAIL_INPUT = (By.NAME, "email")
        CHECKBOX = (By.XPATH, "//label[@for='tcb-consent-tve-u-16390cc253e']")        
        DOWNLOAD_WHITEPAPER_BUTTON = (By.XPATH, "//a[@href='/whitepapers/how-to-test-the-test-automation-framework/'][normalize-space()='Download this papper']")        
        DOWNLOAD_CHEAT_SHEET_BUTTON = (By.XPATH, "//a[@href='/applications/most-complete-appium-java-cheat-sheet'][normalize-space()='Download cheat sheet']")
        CONTENT = (By.ID, "page-content")
        CONTENT_tags_h4 = (By.TAG_NAME, "h4")
        CONTENT_tags_p = (By.TAG_NAME, "p")
        

        print("---- Resources page ----")
        
        # Accept cookies
        def cookies(self):
            cookies = self.driver.find_element(*Resources.COOKIE)
            cookies.click()
            print("Cookies accepted")
            time.sleep(1)
            print("")


        # Back to Resources page
        def back_to_Resources_page(self):
            self.driver.get("https://www.automatetheplanet.com/resources/")
            print("")
            print("Back to Resources clicked")    


        # Search for whitepaper
        def search(self):
            print("Search section")
            search_input = self.driver.find_element(*Resources.SEARCH)
            search_input.send_keys("Whitepaper")
            print("Whitepaper entered")
            time.sleep(2)

            search_button = self.driver.find_element(*Resources.SEARCH_BUTTON)
            self.driver.execute_script("arguments[0].click();", search_button)
            time.sleep(8)
            print("Search button clicked")
            print("search page opened", self.driver.current_url)
            print("")

        
        # Download  papper section
        def download_paper_button(self, name_input, email_input):
            download_paper_button = self.driver.find_element(*Resources.DOWNLOAD_PAPER_BUTTON)
            download_paper_button.click()
            print("Download this papper clicked")
            time.sleep(1)
            print("")

            name = self.driver.find_element(*Resources.NAME_INPUT)
            name.send_keys(name_input)
            print("Name entered")
            time.sleep(2)

            email = self.driver.find_element(*Resources.EMAIL_INPUT)
            email.send_keys(email_input)
            print("Email entered")
            time.sleep(2)

            checkbox = self.driver.find_element(*Resources.CHECKBOX)
            self.driver.execute_script("arguments[0].click();", checkbox)   
            time.sleep(2)
            print("Consent accepted")
            time.sleep(2)

            submit = self.driver.find_element(By.XPATH, "//button[text()='Download Whitepaper']")
            self.driver.execute_script("arguments[0].click();", submit)
            print("Whitepaper downloaded")
            time.sleep(2)


            current_url = self.driver.current_url
            print("Current URL:", current_url)
            if current_url == "https://www.automatetheplanet.com/applications/most-complete-appium-java-cheat-sheet/":
                print("Whitepaper downloaded")
            else:
                print("Whitepaper not downloaded")
            print("")    

            self.driver.get("https://www.automatetheplanet.com/resources/")

                
        # Download Cheat sheet
        def download_cheat_sheet_button(self, name_input, email_input):
            download_cheat_sheet_button = self.driver.find_element(*Resources.DOWNLOAD_CHEAT_SHEET_BUTTON)
            download_cheat_sheet_button.click()
            print("Download cheat sheet clicked")
            time.sleep(1)        

            name = self.driver.find_element(*Resources.NAME_INPUT)
            name.send_keys(name_input)
            print("Name entered")
            time.sleep(2)

            email = self.driver.find_element(*Resources.EMAIL_INPUT)
            email.send_keys(email_input)
            print("Email entered")
            time.sleep(2)

            consent_checkbox = self.driver.find_element(*Resources.CHECKBOX)
            self.driver.execute_script("arguments[0].click();", consent_checkbox)
            print("Consent accepted")
            time.sleep(2)

            current_url = self.driver.current_url
            print("Current URL:", current_url)
            if current_url == "https://www.automatetheplanet.com/privacy-policy/":
                print("Cheat sheet downloaded")
            else:
                print("Cheat sheet not downloaded")
            print("")    


            self.driver.get("https://www.automatetheplanet.com/resources/")



        # Learn more buttons
        def click_all_Learn_more(self):
            learn_more = self.driver.find_elements(By.LINK_TEXT, "Learn more")
            for button in learn_more:
                self.driver.execute_script("arguments[0].click();", button)
                print(button.get_attribute("href"))
                print("Learn more button clicked")
                time.sleep(3)
                self.driver.get("https://www.automatetheplanet.com/resources/")
                print("")


        # Content    
        def content(self):
            print("Content h4")
            content = self.driver.find_element(*Resources.CONTENT) 
            content_tags = content.find_elements(*Resources.CONTENT_tags_h4) 
            for links in content_tags:
                print(links.text)
                time.sleep(1)

            print("Content p")
            content = self.driver.find_element(*Resources.CONTENT) 
            content_tags_p = content.find_elements(*Resources.CONTENT_tags_p) 
            for links in content_tags_p:
                print(links.text)
                time.sleep(1)
            print("")






