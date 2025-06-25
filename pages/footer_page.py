from selenium.webdriver.common.by import By
import time

class Home:   
        def __init__(self, driver):
         self.driver = driver


        # Locators 
        COOKIE =  (By.ID, "cookie_action_close_header")
        FOOTER = (By.ID, "footer")
        FOOTER_LINKS = (By.CSS_SELECTOR, "#footer a")
        SOCIAL_LINKS = (By.CSS_SELECTOR, ".social-links a")

        
        print("---- Footer Page ----")
        
        # Cookies Accept
        def cookies(self):
            cookies = self.driver.find_element(*Home.COOKIE)
            cookies.click()
            print("Cookies accepted")
            time.sleep(1)
        print("")  


        # Footer
        def footer(self):
            print("Footer")
            footer = self.driver.find_element(*Home.FOOTER)
            footer_links = footer.find_elements(*Home.FOOTER_LINKS)
            for link in footer_links:
                print(link.text)
                time.sleep(2)
            print("")   


        # Footer links clicking test 
        def footer_links(self):
            print("Clicking all footer links...")

            # Get all hrefs first to avoid stale elements after back()
            footer = self.driver.find_element(*self.FOOTER)
            links = footer.find_elements(*self.FOOTER_LINKS)
            hrefs = [link.get_attribute("href") for link in links if link.get_attribute("href")]

            for href in hrefs:
                try:
                    footer = self.driver.find_element(*self.FOOTER)
                    self.driver.execute_script("arguments[0].scrollIntoView();", footer)

                    # Find link again using href
                    link = footer.find_element(By.XPATH, f".//a[@href='{href}']")

                    link_text = link.text or href
                    print("Clicking link:", link_text)

                    # Use JS click to avoid click interception
                    self.driver.execute_script("arguments[0].click();", link)

                    time.sleep(8)
                    print("Current URL:", self.driver.current_url)

                    self.driver.back()
                    time.sleep(8)

                except Exception as e:
                    print(f"Error clicking link {href}: {e}")
            print("Finished clicking all footer links.")
            print("")
        print("")    

       
        # Social media section
        def social_media(self):
            print("Clicking all social media links...")
            social_section = self.driver.find_element(*self.FOOTER)
            self.driver.execute_script("arguments[0].scrollIntoView();", social_section)
            links = social_section.find_elements(*self.SOCIAL_LINKS)

            for i in range(len(links)):
                social_section = self.driver.find_element(*self.FOOTER)
                links = social_section.find_elements(*self.SOCIAL_LINKS)
                url = links[i].get_attribute("href")
                print("Opening social link:", url)
                self.driver.execute_script("window.open(arguments[0]);", url)
                time.sleep(5)
                self.driver.switch_to.window(self.driver.window_handles[-1])
                print("Opened URL:", self.driver.current_url)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                print("")
            print("")    

