import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver


from pages.sign_up_page import signup

driver = webdriver.Firefox() 
driver.get("https://app.hubspot.com/login/?loginRedirectUrl=https%3A%2F%2Fapp.hubspot.com%2Fsignup-hubspot%2Fsales%3Futm_medium%3Dvirality%26utm_campaign%3Dhubspot-meetings-embedded-virality%26step%3Dlanding_page")
# maximize_window
driver.maximize_window()

signup_page = signup(driver)

signup_page.cookie_accept()
signup_page.username(
    user_name_input="thaushinishara10222@gmail.com",
    signup_email_input="tharushinishara10222@gmail.com" 
)
