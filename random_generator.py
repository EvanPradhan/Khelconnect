import random
import string

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

# Generate random Nepali names
# List of common Nepali first names
first_names = [
    "Suman", "Ramesh", "Dipesh", "Rajesh", "Bishal", "Rajendra", "Suresh",
    "Bikash", "Rajendra", "Raju", "Mina", "Ram", "Sarvesh", "Chhabi", "Jenish",
    "Suraj", "Deepak", "Asha", "Prakash", "Bimal", "Gita", "Rajani", "Ramlal", "Ramu",
    "Abinash", "Manish", "Pratik", "Niranjan", "Dibya", "Samir", "Abhay", "Santosh",
    "Umesh", "Rajaram", "Sagar", "Rajesh", "Sudha", "Rajendra", "Shyam", "Rabi", "Harka", "Balen",
    "Lalit", "Gyanendra", "Aasif", "Aarif", "Ananta", "Kiran","Anmol", "Bhuwan", "Bikram", "Bishnu",
    "Daya", "Abhijeet", "Pradeep", "Somal", "Kushal", "Bishal", "Aashal", "Kamal", "Virat", "Shikhar"
]

# List of common Nepali last names
last_names = [
    "Shrestha", "Gurung", "Khadka", "Thapa", "Lama", "Basnet", 
    "Adhikari", "Rai", "Magar", "Karki", "Bhattarai", "Poudel", 
    "Chaudhary", "KC", "Pandey", "Nepali", "Gautam", "Dangol",
    "Thapa", "Maharjan", "Pradhan", "Sharma", "Bhandari", "Koirala",
    "Bhurtel", "Khanal", "Khadka", "Bista", "Rai", "KC", "Tharu", "Bhandari",
    "Panta", "Pradhan", "Adhikari", "Dhakal", "Lamichhane", "Oli", "Bhattachan",
    "Bhatta", "Bhatt", "Bhattacharya", "Bhattacharjee", "Bhattacharya", "Lama", "Sherpa",
    "Tamang", "Thapa", "Thapa Magar", "Thapa Chhetri", "Gharti", "Tiwari", "Gole", "Gautam",
    "Shah", "Sah", "Saha"
]

# Function to generate a random Nepali full name
# def generate_nepali_name():
#     first_name = random.choice(first_names)
#     last_name = random.choice(last_names)
#     return f"{first_name} {last_name}"

# Generate random Nepali first Name
def generate_random_nepali_first_name():
    first_name = random.choice(first_names)
    return f"{first_name}"

# Generate random Nepali Last Name
def generate_random_nepali_last_name():
    last_name = random.choice(last_names)
    return f"{last_name}"
# Generate a list of Nepali names
# nepali_names = [generate_nepali_name() for _ in range(10)]
# for name in nepali_names:
#     print(name)


#Generate Random Nepali District
# List of all 77 districts of Nepal
districts = [
    "Achham", "Arghakhanchi", "Baglung", "Baitadi", "Bajhang", "Bajura", "Banke", "Bara",
    "Bardiya", "Bhaktapur", "Bhojpur", "Chitwan", "Dadeldhura", "Dailekh", "Dang", "Darchula",
    "Dhading", "Dhankuta", "Dhanusha", "Dolakha", "Dolpa", "Doti", "Eastern Rukum", "Gorkha",
    "Gulmi", "Humla", "Ilam", "Jajarkot", "Jhapa", "Jumla", "Kailali", "Kalikot", "Kanchanpur",
    "Kapilvastu", "Kaski", "Kathmandu", "Kavrepalanchok", "Khotang", "Lalitpur", "Lamjung",
    "Mahottari", "Makwanpur", "Manang", "Morang", "Mugu", "Mustang", "Myagdi", "Nawalpur",
    "Nuwakot", "Okhaldhunga", "Palpa", "Panchthar", "Parasi", "Parbat", "Parsa", "Pyuthan",
    "Ramechhap", "Rasuwa", "Rautahat", "Rolpa", "Rupandehi", "Salyan", "Sankhuwasabha", 
    "Saptari", "Sarlahi", "Sindhuli", "Sindhupalchok", "Siraha", "Solukhumbu", "Sunsari",
    "Surkhet", "Syangja", "Tanahun", "Taplejung", "Terhathum", "Udayapur", "Western Rukum"
]

# Function to generate a random district
def generate_random_district():
    return random.choice(districts)


# Generate Gorkha City
cities = [
    "Palung", "Aanppipal", "Aaru Arbang", "Aaru Chautara", "Aaru Ghyang", "Aaru Khola",
    "Barpak", "Laprak", "Sulikot", "Siranchok", "Ajirkot", "Chumanuwri", "Dharche",
    "Bhachhek", "Lapu", "Sirdibas"
]
def generate_gorkha_city():
    return random.choice(cities)


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