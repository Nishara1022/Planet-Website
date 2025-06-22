import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.resources_page import Resources 

driver = webdriver.Firefox() 
driver.get("https://www.automatetheplanet.com/resources/")
driver.maximize_window()

home = Resources(driver) 


home.cookies()
home.search()
home.back_to_Resources_page()
home.click_all_Learn_more()
home.download_paper_button(
    name_input="Nishara Tharu",
    email_input="tharushinishara1022@gmail.com")
home.download_cheat_sheet_button(
    name_input="Nishara Tharu",
    email_input="tharushinishara1022@gmail.com")
home.content()
