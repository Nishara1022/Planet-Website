import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver


from pages.create_meeting_page import CreateMeetingBookingPage

driver = webdriver.Chrome() 
driver.get("https://app.hubspot.com/signup-hubspot/sales?utm_medium=virality&utm_campaign=hubspot-meetings-embedded-virality&step=landing_page")


booking_page = CreateMeetingBookingPage(driver)

booking_page.open_page()
booking_page.accept_initial_cookies()
booking_page.enter_email("tharushinishara1022@gmail.com")
booking_page.click_verify_email()
booking_page.manage_cookies()
booking_page.accept_all_cookies()

