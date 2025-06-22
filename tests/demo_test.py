import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.demo_page import DemoPage

driver = webdriver.Chrome() 
driver.get("https://app.hubspot.com/login/?loginRedirectUrl=https%3A%2F%2Fapp.hubspot.com%2Fsignup-hubspot%2Fsales%3Futm_medium%3Dvirality%26utm_campaign%3Dhubspot-meetings-embedded-virality%26step%3Dlanding_page")
# maximize_window
driver.maximize_window()

signup_page = DemoPage(driver)

try:
    signup_page.cookie_accept()
    signup_page.username("thaushinishara10222@gmail.com")
    signup_page.sign_up()
    signup_page.click_demo_button()
    signup_page.fill_demo_form(
    firstname="Nishara",
    lastname="Tharushi",
    email="tharushinishara1022@gmail.com",
    phone="0702242491",
    company="HubSpot",
    website="www.hubspot.com",
    employees="26 to 50",
    country="Cyprus"
    )

    

    #signup_page.close_iframe()
    
except Exception as e:
    print(e)
