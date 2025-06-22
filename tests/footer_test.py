import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver


from pages.footer_page import Home

driver = webdriver.Firefox() 
driver.get("https://www.automatetheplanet.com/")


home = Home(driver) 


home.cookies()

home.footer()
home.footer_links()
home.social_media()
driver.close()
