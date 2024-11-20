from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from faker import Faker
import pyautogui
from itertools import count
from selenium.webdriver.common.keys import Keys
import random
import string
from random_generator import generate_random_contact_number, generate_random_email, generate_random_number, generate_random_nepali_first_name, generate_random_nepali_last_name
from random_generator import generate_random_district, generate_random_number

# Generate random Nepali address
def generate_random_nepali_address():
    # Sample data for streets, areas, and locations in Nepal
    streets = [
        "Raja Birendra Marg", "Prithvi Highway", "Bhupi Sherchan Marg", 
        "Narayan Gopal Chowk", "Durbar Marg", "Siddhartha Marg", 
        "Bagmati Marg", "B.P. Koirala Marg", "Ratna Marg"
    ]
    
    areas = [
        "Dallu", "Baneshwor", "Kumaripati", "Sundhara", "Kalanki", 
        "Maitidevi", "Koteshwor", "Lagankhel", "Gaushala", "Maharajgunj"
    ]
    
    # Generate random values
    street = random.choice(streets)
    area = random.choice(areas)
    ward_number = random.randint(1, 32)  # Ward numbers typically range from 1 to 32
    
    # Combine into a full address
    address = f"{street}, {area}-{ward_number}"
    return address

# Generate Gorkha City
cities = [
    "Palung", "Aanppipal", "Aaru Arbang", "Aaru Chautara", "Aaru Ghyang", "Aaru Khola",
    "Barpak", "Laprak", "Sulikot", "Siranchok", "Ajirkot", "Chumanuwri", "Dharche",
    "Bhachhek", "Lapu", "Sirdibas"
]
def generate_gorkha_city():
    return random.choice(cities)

# Generate random Sports
games = [
    "Cricket", "Football", "Badminton", "Athletics"
]
def generate_random_sport():
    return random.choice(games)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://school-dev.khelconnect.com/login")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(3)

#Login Page Form Fill
# Select Municipality
driver.find_element(*(By.XPATH,"//select[@name='organizer_id']")).click()
driver.find_element(*(By.XPATH,"//option[normalize-space()='Gorkha Sports Council']")).click()
# time.sleep(3)
#Select School
driver.find_element(*(By.XPATH,"//select[@name='school_id']")).click()
driver.find_element(*(By.XPATH, "//option[contains(text(), 'Sulikot Gaunpalika')]")).click()
# time.sleep(3)
# Enter Username and Password
driver.find_element(*(By.XPATH,"//input[@placeholder='Please Enter Username']")).send_keys("sulikotgaunpalikaadmin")
driver.find_element(*(By.XPATH,"//input[@placeholder='Please Enter Password']")).send_keys("Admin!123")

#enter login
driver.find_element(*(By.XPATH,"//button[normalize-space()='Login']")).click()
time.sleep(3)

# Click People and player
driver.find_element(*(By.XPATH,"8")).click()
driver.find_element(*(By.XPATH,"//div[@class='css-7a2b4p']//div[2]")).click()

for i in range(0,2):
    # Create player
    # Click on create
    driver.find_element(*(By.XPATH,"//button[normalize-space()='Create']")).click()

    # Personal Information
    faker = Faker()
    # names = (faker.first_name() for _ in count())

    # name = next(name for name in names
    #             if len(name) == 10)
    first_name = driver.find_element(*(By.XPATH,"//input[@placeholder='First Name']"))
    first_name.send_keys(generate_random_nepali_first_name())

    # middle_name = driver.find_element(*(By.XPATH,"//input[@placeholder='Middle Name']"))
    # middle_name.send_keys(faker.middle_name())

    last_name = driver.find_element(*(By.XPATH,"//input[@placeholder='Last Name']"))
    last_name.send_keys(generate_random_nepali_last_name())

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

    driver.find_element(*(By.XPATH,"//div[@class='react-datepicker__week']/div[contains(text(), '12')]")).click()

    # Gender
    driver.find_element(*(By.XPATH,"//label[1]//span[1]")).click()

    # Nationality and region
    driver.find_element(*(By.XPATH,"//select[@name='main_nationality']")).click()
    driver.find_element(*(By.XPATH,"//select[@name='main_nationality']/option[contains(text(), 'Nepal')]")).click()

    driver.find_element(*(By.XPATH,"//select[@name='country_of_birth']")).click()
    driver.find_element(*(By.XPATH, "//select[@name='country_of_birth']/option[@value='Nepal']")).click()

    driver.find_element(*(By.XPATH,"//input[@placeholder='Region or state of birth']")).send_keys("Gorkha")

    driver.find_element(*(By.XPATH,"//input[@placeholder='City of birth']")).send_keys(generate_gorkha_city())

    # Additional Information
    driver.find_element(*(By.XPATH,"//input[@placeholder='Identification Document Number']")).send_keys(generate_random_number())
    driver.find_element(*(By.XPATH,"//input[@name='fathers_citizenship_number']")).send_keys(generate_random_number())

    # Click Next button
    driver.find_element(*(By.XPATH,"//button[normalize-space()='Next']")).click()
    time.sleep(2)

    #Contact Details
    # Address

    prim_add = driver.find_element(*(By.XPATH,"//input[@placeholder='Primary address']"))
    prim_add.send_keys(generate_random_nepali_address())

    # second_add = driver.find_element(*(By.XPATH,"//input[@placeholder='Secondary Address']"))
    # second_add.send_keys(faker.address())

    # Country and district
    country = driver.find_element(*(By.XPATH,"//select[@name='country']"))
    country.click()
    driver.find_element(*(By.XPATH, "//option[@value='Nepal']")).click()
    time.sleep(2)

    district = driver.find_element(*(By.XPATH,"//input[@placeholder='District']"))
    district.send_keys("Gorkha")

    city = driver.find_element(*(By.XPATH,"//input[@placeholder='City']"))
    city.send_keys(generate_gorkha_city())

    # Contact info
    contact_num = driver.find_element(*(By.XPATH,"//input[@placeholder='Contact Number']"))
    contact_num.send_keys(generate_random_contact_number())
    time.sleep(2)

    driver.find_element(*(By.XPATH,"//*[name()='path' and contains(@d,'M1 12.0071')]")).click()
    time.sleep(2)

    # Registration
    # handling Searchable Multiselect dropdown 
    sports = driver.find_element(*(By.XPATH,"//input[@class=' css-10g7vpn']"))
    sports.click()
    time.sleep(2)

    sports.send_keys(generate_random_sport()) 
    time.sleep(2) 
    sports.send_keys(Keys.ENTER) 
    time.sleep(2) 
    sports.click() 
    time.sleep(2) 
    sports.send_keys(generate_random_sport()) 
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

    # Documents
    # Passport sized photo
    pp_photo = driver.find_element(*(By.XPATH,"//div[@class='css-qrllub']//div[2]//div[1]//div[1]//p[1]"))
    pp_photo.click()
    time.sleep(3)
    file_path = r"C:\Users\user\Desktop\QA content\Photos\passport_photo.jpg"
    pyautogui.write(file_path)
    pyautogui.press('enter')
    time.sleep(3)

    # Identification document
    id_photo = driver.find_element(*(By.XPATH,"/html/body/div[1]/main/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div[3]/div/div/p"))
    id_photo.click()
    time.sleep(3)
    file_path = r"C:\Users\user\Desktop\QA content\Photos\id_photo.jpg"
    pyautogui.write(file_path)
    pyautogui.press('enter')
    time.sleep(3)

    # Click Next
    driver.find_element(*(By.XPATH,"//button[normalize-space()='Next']")).click()

    # Click Finish
    driver.find_element(*(By.XPATH,"//button[normalize-space()='Finish']")).click()

driver.close()
driver.quit()