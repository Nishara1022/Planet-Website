from selenium.webdriver.common.by import By
import time

class PrivateTraining:
    def __init__(self, driver):
        self.driver = driver
        

    # locators
    COOKIE = (By.ID, "cookie_action_close_header")
    FUNDEMENTAL = (By.XPATH, "//a[@href='#floating-license']")
    ANTON = (By.XPATH, "//a[@href='#anton-angelov']")
    CONTENT = (By.ID, "tech-cat-wrap")
    CONTENT2 = (By.ID, "page-content")
    
    
    print("---- Private Training page ----")
    # accept cookies
    def cookies(self):
            cookies = self.driver.find_element(*PrivateTraining.COOKIE)
            cookies.click()
            print("Cookies accepted")
            time.sleep(1)
            print("")


    # fundamentals
    def fundementals(self):   
        self.driver.find_element(*PrivateTraining.FUNDEMENTAL).click()
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*PrivateTraining.ANTON))
        print("Fundamentals clicked")
        time.sleep(2)

    
    # anton
    def anton(self):
        self.driver.find_element(*PrivateTraining.ANTON).click()
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*PrivateTraining.FUNDEMENTAL))
        print("Anton clicked")
        time.sleep(2)
        print("")

   
    # content
    def content(self):
        print("---- Content h3 ----")
        content = self.driver.find_element(*PrivateTraining.CONTENT) 
        for links in content.find_elements(By.TAG_NAME, "h3"):
            print(links.text)
            time.sleep(1)
        print("")
            
        print("---- Content p ----")
        content = self.driver.find_element(*PrivateTraining.CONTENT)
        for links in content.find_elements(By.TAG_NAME, "p"):
            print(links.text)
            time.sleep(1)
        print("")


        print("---- Content ul ----")
        content = self.driver.find_element(*PrivateTraining.CONTENT)
        for links in content.find_elements(By.TAG_NAME, "ul"):
            print(links.text)
            time.sleep(1)
        print("")

        print("---- Content li ----")
        content = self.driver.find_element(*PrivateTraining.CONTENT)
        for links in content.find_elements(By.TAG_NAME, "li"):
            print(links.text)
            time.sleep(1)
        print("")


        print("---- Content a ----")
        content = self.driver.find_element(*PrivateTraining.CONTENT)
        for links in content.find_elements(By.TAG_NAME, "a"):
            print(links.text)
            time.sleep(1)
        print("")


       
    def content2(self):
        print("---- Content section 2 h3 ----")
        content = self.driver.find_element(*PrivateTraining.CONTENT2) 
        content_tags = content.find_elements(By.TAG_NAME, "h3") 
        for links in content_tags:
            print(links.text)
            links.click()
            time.sleep(1)
        print("\n")


        print("---- Content p ----")
        content = self.driver.find_element(*PrivateTraining.CONTENT2) 
        content_tags = content.find_elements(By.TAG_NAME, "p") 
        for links in content_tags:
            print(links.text)
            time.sleep(1)
        print("\n")


        print("---- Content 2 ul ----")
        content = self.driver.find_element(*PrivateTraining.CONTENT2) 
        content_tags = content.find_elements(By.TAG_NAME, "ul") 
        for links in content_tags:
            print(links.text)
            time.sleep(1)
        print("")


        print("---- Content 2 li ----")
        content = self.driver.find_element(*PrivateTraining.CONTENT2) 
        content_tags = content.find_elements(By.TAG_NAME, "li") 
        for links in content_tags:
            print(links.text)
            time.sleep(1)
        print("")


