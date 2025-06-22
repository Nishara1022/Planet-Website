import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver


from pages.home_page import Home

driver = webdriver.Firefox() 
driver.get("https://www.automatetheplanet.com/")


home = Home(driver) 


home.cookies()
home.logo()
home.header()
home.back_to_home()
home.contact()
home.back_to_home()
home.first_contact()
home.back_to_home()

home.readfull_story()
home.back_to_home()

home.read_full_article()
home.back_to_home()

home.web_automation()
home.back_to_home()
home.desktop_automation()
home.back_to_home()
home.api_automation()
home.back_to_home()
home.mobile_automation()
home.back_to_home()
home.private_training()
home.back_to_home()

home.start_the_test_section()
home.back_to_home()

home.book_a_meeting_section()

home.content()
home.TAB_content_h3()
home.TAB_content_p()
home.how_can_we_help_h4()
home.how_can_we_help_p()
home.Right_SetUph4()
home.Right_SetUpP()






