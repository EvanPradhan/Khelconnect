from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import random
import pyautogui
from random_generator import generate_random_contact_number, generate_random_nepali_first_name, generate_random_email

def generate_random_sport():
    sport = [
        "Badminton", "Athletics", "Cricket", "Football"
        ]
    return random.choice(sport)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://municipal-dev.khelconnect.com/login")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(3)

# School Login
# Select Sports Council
driver.find_element(*(By.XPATH, "//select[@name='organizer_id']")).click()   # Click Sports Council dropdown
sports_council = driver.find_element(*(By.XPATH, "//option[contains (text(), 'Kathmandu Municipality')]"))
sports_council.click()

# Enter Username and Password and Click Login
username = driver.find_element(*(By.XPATH, "//input[@name='username']"))
username.send_keys("organizer1")

password = driver.find_element(*(By.XPATH, "//input[@name='password']"))
password.send_keys("Admin!123")

login = driver.find_element(*(By.XPATH, "//button[@type='submit']"))
login.click()

# Click on Competitions from sidebar
driver.find_element(*(By.XPATH,"//a[normalize-space()='Competition']")).click()
time.sleep(2)

# Click on Create button
driver.find_element(*(By.XPATH, "//button[normalize-space()='Create']")).click()

# Fill up the form for Competition Creation
comp_title = driver.find_element(*(By.XPATH, "//input[@placeholder='Competition Title']"))
comp_title.send_keys("Test 19")

abbrev = driver.find_element(*(By.XPATH, "//input[@placeholder='Abbreviation']"))
abbrev.send_keys("Test")

sports = driver.find_element(*(By.XPATH, "//input[@class=' css-10g7vpn']"))
sports.click()

game1 = generate_random_sport()
game2 = generate_random_sport()

sports.send_keys(game1)
sports.send_keys(Keys.ENTER)

sports.send_keys(game2)
sports.send_keys(Keys.ENTER)

description = driver.find_element(*(By.XPATH, "//textarea[@placeholder='Description']"))
description.send_keys("This is Competition created")

# File Upload
logo = driver.find_element(*(By.XPATH,"//div[6]//div[1]//div[1]//p[1]"))
logo.click()
time.sleep(2)
file_path = r"C:\Users\user\Desktop\QA content\Photos\id_photo.jpg"
pyautogui.write(file_path)
pyautogui.press('enter')
time.sleep(3)

# Click Next
driver.find_element(*(By.XPATH, "//button[contains (text(), 'Next')]")).click()
time.sleep(2)

# Add Contact details
name = driver.find_element(*(By.XPATH,"//input[@placeholder='Name']"))
name.send_keys(generate_random_nepali_first_name())

contact_number = driver.find_element(*(By.XPATH,"//input[@placeholder='Contact Number']"))
contact_number.send_keys(generate_random_contact_number())

email = driver.find_element(*(By.XPATH,"//input[@placeholder='Email']"))
email.send_keys(generate_random_email())

cont_sports = driver.find_element(*(By.XPATH, "/html/body/div[1]/main/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div[1]/div/div/div/div/div[5]/div/div/div/div[1]/div[1]/div[2]/input"))
cont_sports.click()

cont_sports.send_keys(game1)
cont_sports.send_keys(Keys.ENTER)

cont_sports.send_keys(game2)
cont_sports.send_keys(Keys.ENTER)

comp_manager = driver.find_element(*(By.XPATH, "//select[@name='contact_details.0.competition_manager']"))
comp_manager.click()
driver.find_element(*(By.XPATH,"//option[@value='coach']")).click()

# Click Next
driver.find_element(*(By.XPATH, "//button[contains (text(), 'Next')]")).click()
time.sleep(2)

# Tournament Create
tourn_sport = driver.find_element(*(By.XPATH, "//input[@class=' css-10g7vpn']"))
tourn_sport.click()

tourn_sport.send_keys(game1)
tourn_sport.send_keys(Keys.ENTER)

driver.close()
driver.quit()