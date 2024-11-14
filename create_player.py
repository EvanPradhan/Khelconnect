from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random
import string
from faker import Faker
import pyautogui
from itertools import count
from selenium.webdriver.common.keys import Keys

# Generate random contact number
def generate_random_contact_number():
   return "98"+''.join(random.choices(string.digits, k=8))

# Generate random contact mail
def generate_random_email():
    domain = "gmail.com"
    email_length = 5
    random_string = ''.join(random.choice(string.ascii_lowercase)for _ in range(email_length))
    return random_string + "@"+domain

# Generate random number
def generate_random_number():
    return ''.join(random.choices(string.digits, k=5))

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://school-dev.khelconnect.com/login")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(3)

#Login Page Form Fill
# Select Municipality
driver.find_element(*(By.XPATH,"//select[@name='organizer_id']")).click()
driver.find_element(*(By.XPATH,"//option[normalize-space()='Kathmandu Municipality']")).click()
# time.sleep(3)
#Select School
driver.find_element(*(By.XPATH,"//select[@name='school_id']")).click()
driver.find_element(*(By.XPATH, "//option[contains(text(), 'DEV test 28')]")).click()
# time.sleep(3)
# Enter Username and Password
driver.find_element(*(By.XPATH,"//input[@placeholder='Please Enter Username']")).send_keys("devtest28")
driver.find_element(*(By.XPATH,"//input[@placeholder='Please Enter Password']")).send_keys("Admin!123")

#enter login
driver.find_element(*(By.XPATH,"//button[normalize-space()='Login']")).click()
time.sleep(3)

# Click People and player
driver.find_element(*(By.XPATH,"//p[@class='chakra-text css-1nhpy1b']")).click()
driver.find_element(*(By.XPATH,"//div[@class='css-7a2b4p']//div[2]")).click()

# Create player
# Click on create
driver.find_element(*(By.XPATH,"//button[normalize-space()='Create']")).click()

# Personal Information
faker = Faker()
names = (faker.first_name() for _ in count())

name = next(name for name in names
            if len(name) == 10)
first_name = driver.find_element(*(By.XPATH,"//input[@placeholder='First Name']"))
first_name.send_keys(name)

# middle_name = driver.find_element(*(By.XPATH,"//input[@placeholder='Middle Name']"))
# middle_name.send_keys(faker.middle_name())

last_name = driver.find_element(*(By.XPATH,"//input[@placeholder='Last Name']"))
last_name.send_keys(faker.last_name())

# Date of Birth and date of admission
dob = driver.find_element(*(By.XPATH,"//div[5]//div[1]//div[1]//div[1]//div[1]//input[1]"))
dob.click()
driver.find_element(*(By.XPATH,"//div[@class='css-0']//div[1]//select[1]")).click()
driver.find_element(*(By.XPATH, "//option[contains(text(), '1999')]")).click()

driver.find_element(*(By.XPATH,"//div[@class='css-0']//div[1]//select[1]")).click()
driver.find_element(*(By.XPATH, "//option[contains(text(), 'June')]")).click()

driver.find_element(*(By.XPATH,"//div[@class='react-datepicker__week']/div[contains(text(), '12')]")).click()
# Date of admission
driver.find_element(*(By.XPATH, "//*[@id='app']/main/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div[6]/div/div/div[1]/div/input")).click()
driver.find_element(*(By.XPATH,"//div[@class='css-0']//div[1]//select[1]")).click()
driver.find_element(*(By.XPATH, "//option[contains(text(), '2021')]")).click()

driver.find_element(*(By.XPATH,"//div[@class='css-0']//div[1]//select[1]")).click()
driver.find_element(*(By.XPATH, "//option[contains(text(), 'April')]")).click()

driver.find_element(*(By.XPATH,"//div[@class='react-datepicker__week']/div[contains(text(), '21')]")).click()

# Gender
driver.find_element(*(By.XPATH,"//label[1]//span[1]")).click()

# Nationality and region
driver.find_element(*(By.XPATH,"//select[@name='main_nationality']")).click()
driver.find_element(*(By.XPATH,"//select[@name='main_nationality']/option[contains(text(), 'Nepal')]")).click()

driver.find_element(*(By.XPATH,"//select[@name='country_of_birth']")).click()
driver.find_element(*(By.XPATH, "//select[@name='country_of_birth']/option[@value='India']")).click()

driver.find_element(*(By.XPATH,"//input[@placeholder='Region or state of birth']")).send_keys(faker.state())

driver.find_element(*(By.XPATH,"//input[@placeholder='City of birth']")).send_keys(faker.city())

# Additional Information
driver.find_element(*(By.XPATH,"//input[@placeholder='Identification Document Number']")).send_keys(generate_random_number())
driver.find_element(*(By.XPATH,"//input[@name='fathers_citizenship_number']")).send_keys(generate_random_number())

# Click Next button
driver.find_element(*(By.XPATH,"//button[normalize-space()='Next']")).click()
print("Personal Information Done")
time.sleep(3)

#Contact Details
# Address
prim_add = driver.find_element(*(By.XPATH,"//input[@placeholder='Primary address']"))
prim_add.send_keys(faker.address())

second_add = driver.find_element(*(By.XPATH,"//input[@placeholder='Secondary Address']"))
second_add.send_keys(faker.address())

# Country and district
country = driver.find_element(*(By.XPATH,"//select[@name='country']"))
country.click()
driver.find_element(*(By.XPATH, "//option[@value='Nepal']")).click()
time.sleep(2)

district = driver.find_element(*(By.XPATH,"//input[@placeholder='District']"))
district.send_keys("Lalitpur")

city = driver.find_element(*(By.XPATH,"//input[@placeholder='City']"))
city.send_keys("Satdobato")

# Contact info
contact_num = driver.find_element(*(By.XPATH,"//input[@placeholder='Contact Number']"))
contact_num.send_keys(generate_random_contact_number())
time.sleep(5)

driver.find_element(*(By.XPATH,"//*[name()='path' and contains(@d,'M1 12.0071')]")).click()
time.sleep(5)
print("Contact details done")

# Registration
# handling Searchable Multiselect dropdown 
sports = driver.find_element(*(By.XPATH,"//input[@id='react-select-2-input']"))
sports.click()
time.sleep(2)

sports.send_keys("Badminton") 
time.sleep(2) 
sports.send_keys(Keys.ENTER) 
time.sleep(2) 
sports.click() 
time.sleep(2) 
sports.send_keys("Athletics") 
time.sleep(2) 
sports.send_keys(Keys.ENTER)

# Sub role
sub_role = driver.find_element(*(By.XPATH,"//select[@name='sub_role']"))
sub_role.click()
driver.find_element(*(By.XPATH,"//option[@value='amateur']")).click()

# Age Group
age_group = driver.find_element(*(By.XPATH,"//select[@name='age_group']"))
age_group.click()
driver.find_element(*(By.XPATH,"//option[@value='18-20']")).click()

driver.find_element(*(By.XPATH,"//button[normalize-space()='Next']")).click()
print("Registration Done")

# Documents
# Passport sized photo
pp_photo = driver.find_element(*(By.XPATH,"//div[@class='css-qrllub']//div[2]//div[1]//div[1]//p[1]"))
pp_photo.click()
time.sleep(3)
file_path = r"C:\Users\user\Desktop\QA content\Photos\passport_photo.jpg"
pyautogui.write(file_path)
pyautogui.press('enter')
time.sleep(5)

# Identification document
id_photo = driver.find_element(*(By.XPATH,"/html/body/div[1]/main/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div[3]/div/div/p"))
id_photo.click()
time.sleep(3)
file_path = r"C:\Users\user\Desktop\QA content\Photos\id_photo.jpg"
pyautogui.write(file_path)
pyautogui.press('enter')
time.sleep(5)

# Click Next
driver.find_element(*(By.XPATH,"//button[normalize-space()='Next']")).click()

driver.close()
driver.quit()