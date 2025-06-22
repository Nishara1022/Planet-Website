import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver


from pages.web_automation_page import WebAutomation

driver = webdriver.Firefox() 
driver.get("https://www.automatetheplanet.com/web-automation/")
driver.maximize_window()

home = WebAutomation(driver) 


home.cookie_accept()
home.tabs()
home.book_a_meeting_form(
    name_input="Nishara Tharu",
    email_input="tharushinishara1022@gmail.com",
    message_input="I am interested in the Regular Automation QA Engineer role"
)

