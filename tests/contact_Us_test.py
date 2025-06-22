import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver


from pages.contact_us_page import Home

driver = webdriver.Firefox() 
driver.get("https://www.automatetheplanet.com/contact-us/")


home = Home(driver) 


home.cookies()

home.contact_us_form(
    name_input="Nishara Tharu",
    email_input="tharushinishara1022@gmail.com",
    message_input="I am interested in the Regular Automation QA Engineer role"
)

