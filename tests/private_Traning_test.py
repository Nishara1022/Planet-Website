import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from pages.private_traning_page import PrivateTraining

driver = webdriver.Chrome() 
driver.get("https://www.automatetheplanet.com/services/private-training/")
# maximize_window
driver.maximize_window()

private = PrivateTraining(driver)

private.cookies()
private.fundementals()
private.anton()
private.content()
private.content2()