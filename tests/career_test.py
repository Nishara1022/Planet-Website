import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.career_page import Career

driver = webdriver.Firefox() 
driver.get("https://www.automatetheplanet.com/careers/")
# maximize_window
driver.maximize_window()

career = Career(driver)

career.cookies()
career.qa()
career.fill_form(
    name="Nishara Tharu",
    email="tharushinishara1022@gmail.com",
    subject="Regular Automation QA Engineer",
    phone="0704567890",
    mesage="I am interested in the Regular Automation QA Engineer role",
    resume = "C:\\Users\\User\\Desktop\\CV\\Nishara 2024 CV blue.pdf")