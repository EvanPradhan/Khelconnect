from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random
import string
from faker import Faker
import pyautogui

data = [ 
        { 
        "username": "palungtarnagarpalikaadmin", 
        "password": "Admin!123", 
        "logo": r"C:\Users\user\Desktop\QA content\Photos\Nagarpalika\palungtar nagarpalika.jpg", 
        "banner": None, 
        "primary_contact_name": "Umesh Thapa", 
        "primary_contact_number": "9812343520", 
        "primary_contact_email": "palungtarnagarpalikaadmin@gmail.com", 
        "primary_contact_position": "Administrator", 
        "secondary_contacts": None, 
        "school_id": 54, 
        "contact_number": "9812828182", 
        "email": "palungtarnagarpalika@gmail.com", 
        "address_1": "Gorkha", 
        "address_2": "Gorkha", 
        "country": "Nepal", 
        "district": "Gorkha", 
        "city": "Gorkha", 
        "emis_number": "12334", 
        }, 

        { 
        "username": "aarughatgaunpalikaadmin", 
        "password": "Admin!123", 
        "logo": r"C:\Users\user\Desktop\QA content\Photos\Nagarpalika\Arughat Gaunpalika.jpg", 
        "banner": None, 
        "primary_contact_name": "Pawan Kumar Shah", 
        "primary_contact_number": "9812343520", 
        "primary_contact_email": "aarughatgaunpalikaadmin@gmail.com", 
        "primary_contact_position": "Administrator", 
        "secondary_contacts": None, 
        "school_id": 55, 
        "contact_number": "9812828182", 
        "email": "aarughatgaunpalika@gmail.com", 
        "address_1": "Gorkha", 
        "address_2": "Gorkha", 
        "country": "Nepal", 
        "district": "Gorkha", 
        "city": "Gorkha", 
        "emis_number": "12334", 
        }, 

        { 
        "username": "bhimsengaunpalikaadmin", 
        "password": "Admin!123", 
        "logo": r"C:\Users\user\Desktop\QA content\Photos\Nagarpalika\Bhimsen Gaunpalika.jpg", 
        "banner": None, 
        "primary_contact_name": "Sajjan Maharjan", 
        "primary_contact_number": "9812343520", 
        "primary_contact_email": "bhimsengaunpalikaadmin@gmail.com", 
        "primary_contact_position": "Administrator", 
        "secondary_contacts": None, 
        "school_id": 56, 
        "contact_number": "9812828182", 
        "email": "bhimsengaunpalika@gmail.com", 
        "address_1": "Gorkha", 
        "address_2": "Gorkha", 
        "country": "Nepal", 
        "district": "Gorkha", 
        "city": "Gorkha", 
        "emis_number": "12334", 
        },

        { 
        "username": "sahidlakhangaunpalikaadmin", 
        "password": "Admin!123", 
        "logo": r"C:\Users\user\Desktop\QA content\Photos\Nagarpalika\Sahid Lakhan Gaunpalika.png", 
        "banner": None, 
        "primary_contact_name": "Abhay Maharjan", 
        "primary_contact_number": "9812343520", 
        "primary_contact_email": "sahidlakhangaunpalikaadmin@gmail.com", 
        "primary_contact_position": "Administrator", 
        "secondary_contacts": None, 
        "school_id": 57, 
        "contact_number": "9812828182", 
        "email": "sahidlakhangaunpalika@gmail.com", 
        "address_1": "Gorkha", 
        "address_2": "Gorkha", 
        "country": "Nepal", 
        "district": "Gorkha", 
        "city": "Gorkha", 
        "emis_number": "12334", 
        },

         { 
        "username": "gandakigaunpalikaadmin", 
        "password": "Admin!123", 
        "logo": r"C:\Users\user\Desktop\QA content\Photos\Nagarpalika\Gandaki Gaunpalika.jpg", 
        "banner": None, 
        "primary_contact_name": "Sameer Kayastha", 
        "primary_contact_number": "9812343520", 
        "primary_contact_email": "gandakigaunpalikaadmin@gmail.com", 
        "primary_contact_position": "Administrator", 
        "secondary_contacts": None, 
        "school_id": 58, 
        "contact_number": "9812828182", 
        "email": "gandakigaunpalika@gmail.com", 
        "address_1": "Gorkha", 
        "address_2": "Gorkha", 
        "country": "Nepal", 
        "district": "Gorkha", 
        "city": "Gorkha", 
        "emis_number": "12334", 
        },
        
        { 
        "username": "chumnubrigaunpalikaadmin", 
        "password": "Admin!123", 
        "logo": r"C:\Users\user\Desktop\QA content\Photos\Nagarpalika\Chum Nubri Gaunpalika.jpeg", 
        "banner": None, 
        "primary_contact_name": "Abinash Pant", 
        "primary_contact_number": "9812343520", 
        "primary_contact_email": "chumnubrigaunpalikaadmin@gmail.com", 
        "primary_contact_position": "Administrator", 
        "secondary_contacts": None, 
        "school_id": 59, 
        "contact_number": "9812828182", 
        "email": "chumnubrigaunpalika@gmail.com", 
        "address_1": "Gorkha", 
        "address_2": "Gorkha", 
        "country": "Nepal", 
        "district": "Gorkha", 
        "city": "Gorkha", 
        "emis_number": "12334", 
        },

         { 
        "username": "siranchokgaunpalikaadmin", 
        "password": "Admin!123", 
        "logo": r"C:\Users\user\Desktop\QA content\Photos\Nagarpalika\Siranchok Gaunpalika.jpg", 
        "banner": None, 
        "primary_contact_name": "Dibya Adhikari", 
        "primary_contact_number": "9812343520", 
        "primary_contact_email": "siranchokgaunpalikaadmin@gmail.com", 
        "primary_contact_position": "Administrator", 
        "secondary_contacts": None, 
        "school_id": 60, 
        "contact_number": "9812828182", 
        "email": "siranchokgaunpalika@gmail.com", 
        "address_1": "Gorkha", 
        "address_2": "Gorkha", 
        "country": "Nepal", 
        "district": "Gorkha", 
        "city": "Gorkha", 
        "emis_number": "12334", 
        },

          { 
        "username": "gorkhanagarpalikaadmin", 
        "password": "Admin!123", 
        "logo": r"C:\Users\user\Desktop\QA content\Photos\Nagarpalika\Gorkha Nagarpalika.jpg", 
        "banner": None, 
        "primary_contact_name": "Niranjan Shrestha", 
        "primary_contact_number": "9812343520", 
        "primary_contact_email": "gorkhanagarpalikaadmin@gmail.com", 
        "primary_contact_position": "Administrator", 
        "secondary_contacts": None, 
        "school_id": 61, 
        "contact_number": "9812828182", 
        "email": "gorkhanagarpalika@gmail.com", 
        "address_1": "Gorkha", 
        "address_2": "Gorkha", 
        "country": "Nepal", 
        "district": "Gorkha", 
        "city": "Gorkha", 
        "emis_number": "12334", 
        },

         { 
        "username": "ajirkotgaunpalikaadmin", 
        "password": "Admin!123", 
        "logo": r"C:\Users\user\Desktop\QA content\Photos\Nagarpalika\Ajirkot Gaunpalika.jpg", 
        "banner": None, 
        "primary_contact_name": "Pratik Dahal", 
        "primary_contact_number": "9812343520", 
        "primary_contact_email": "ajirkotgaunpalikaadmin@gmail.com", 
        "primary_contact_position": "Administrator", 
        "secondary_contacts": None, 
        "school_id": 62, 
        "contact_number": "9812828182", 
        "email": "ajirkotgaunpalika@gmail.com", 
        "address_1": "Gorkha", 
        "address_2": "Gorkha", 
        "country": "Nepal", 
        "district": "Gorkha", 
        "city": "Gorkha", 
        "emis_number": "12334", 
        },

         { 
        "username": "dharchegaunpalikaadmin", 
        "password": "Admin!123", 
        "logo": r"C:\Users\user\Desktop\QA content\Photos\Nagarpalika\Dharche Gaunpalika.jpg", 
        "banner": None, 
        "primary_contact_name": "Manish Ghimire", 
        "primary_contact_number": "9812343520", 
        "primary_contact_email": "dharchegaunpalikaadmin@gmail.com", 
        "primary_contact_position": "Administrator", 
        "secondary_contacts": None, 
        "school_id": 63, 
        "contact_number": "9812828182", 
        "email": "dharchegaunpalika@gmail.com", 
        "address_1": "Gorkha", 
        "address_2": "Gorkha", 
        "country": "Nepal", 
        "district": "Gorkha", 
        "city": "Gorkha", 
        "emis_number": "12334", 
        },

          { 
        "username": "sulikotgaunpalikaadmin", 
        "password": "Admin!123", 
        "logo": r"C:\Users\user\Desktop\QA content\Photos\Nagarpalika\Sulikot Gaunpalika.jpg", 
        "banner": None, 
        "primary_contact_name": "Samragge Rajyalaxmi Shah", 
        "primary_contact_number": "9812343520", 
        "primary_contact_email": "sulikotgaunpalikaadmin@gmail.com", 
        "primary_contact_position": "Administrator", 
        "secondary_contacts": None, 
        "school_id": 64, 
        "contact_number": "9812828182", 
        "email": "sulikotgaunpalika@gmail.com", 
        "address_1": "Gorkha", 
        "address_2": "Gorkha", 
        "country": "Nepal", 
        "district": "Gorkha", 
        "city": "Gorkha", 
        "emis_number": "12334", 
        }
]
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
def generate_random_emis():
    return ''.join(random.choices(string.digits, k=5))

for i in range(0,11):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://school-dev.khelconnect.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        time.sleep(3)

        #click on register
        driver.find_element(*(By.XPATH,"//button[normalize-space()='Register']")).click()
        time.sleep(3)

        #click on school dropdown and select school
        driver.find_element(*(By.XPATH,"//select[@name='school_id']")).click()
        driver.find_element(*(By.XPATH,f"//option[@value='{data[i]["school_id"]}']")).click()
        time.sleep(3)

        #enter contact details
        contact_num = driver.find_element(*(By.XPATH,"//input[@name='contact_number']"))
        contact_num.send_keys(generate_random_contact_number())

        contact_mail = driver.find_element(*(By.XPATH,"//input[@name='email']"))
        contact_mail.send_keys(data[i]['email'])

        emis = driver.find_element(*(By.XPATH,"//input[@name='emis_number']"))
        emis.send_keys(generate_random_emis())
        time.sleep(2)

        admin_username = driver.find_element(*(By.XPATH,"//input[@placeholder='Municipal Admin Username']"))
        admin_username.send_keys(data[i]['username'])

        admin_password = driver.find_element(*(By.XPATH,"//input[@placeholder='Municipal Admin Password']"))
        admin_password.send_keys("Admin!123")

        confirm_password = driver.find_element(*(By.XPATH,"//input[@placeholder='Confirm Municipal Admin Password']"))
        confirm_password.send_keys("Admin!123")

        # Enter Address
        primary_add = driver.find_element(*(By.XPATH,"//input[@name='address_1']"))
        primary_add.send_keys(data[i]['address_1'])

        secondary_add = driver.find_element(*(By.XPATH,"//input[@name='address_2']"))
        secondary_add.send_keys(data[i]['address_2'])

        driver.find_element(*(By.XPATH,"//select[@name='country']")).click()
        driver.find_element(*(By.XPATH,"//option[@value='Nepal']")).click()

        district = driver.find_element(*(By.XPATH,"//input[@name='district']"))
        district.send_keys(data[i]['district'])

        city = driver.find_element(*(By.XPATH,"//input[@name='city']"))
        city.send_keys(data[i]['city'])

        # Primary Contact details
        prim_name = driver.find_element(*(By.XPATH,"//input[@name='primary_contact_name']"))
        prim_name.send_keys(data[i]['primary_contact_name'])

        prim_email = driver.find_element(*(By.XPATH,"//input[@name='primary_contact_email']"))
        prim_email.send_keys(data[i]['primary_contact_email'])

        prim_phone = driver.find_element(*(By.XPATH,"//input[@name='primary_contact_number']"))
        prim_phone.send_keys(generate_random_contact_number())

        prim_position = driver.find_element(*(By.XPATH,"//input[@name='primary_contact_position']"))
        prim_position.send_keys("Director")

        # Secondary Contact details
        # sec_name = driver.find_element(*(By.XPATH,"//input[@name='secondary_contact_name']"))
        # sec_name.send_keys(fake.name())

        # sec_email = driver.find_element(*(By.XPATH,"//input[@name='secondary_contact_email']"))
        # sec_email.send_keys(generate_random_email())

        # sec_phone = driver.find_element(*(By.XPATH,"//input[@name='secondary_contact_number']"))
        # sec_phone.send_keys(generate_random_contact_number())

        # sec_position = driver.find_element(*(By.XPATH,"//input[@name='secondary_contact_position']"))
        # sec_position.send_keys("Manager")

        # File upload
        school_logo = driver.find_element(*(By.XPATH,"//div[26]//div[1]//div[1]//p[1]"))
        school_logo.click()
        time.sleep(3)
        # file_path = r"C:\Users\user\Desktop\QA content\Photos\Nagarpalika\palungtar nagarpalika.jpg"
        file_path = data[i]["logo"]
        pyautogui.write(file_path)
        pyautogui.press('enter')
        time.sleep(10)

        # Click Save
        driver.find_element(*(By.XPATH,"//button[normalize-space()='Save']")).click()
        print(f"complete {data[i]["username"]}")
        time.sleep(2)
        driver.quit()
