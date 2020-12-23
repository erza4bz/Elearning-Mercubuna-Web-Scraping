import mechanicalsoup
import json

browser = mechanicalsoup.StatefulBrowser() # Using StatefulBrowser to start scraping
browser.open("https://elearning.mercubuana.ac.id/") # UMB Elearning URL
browser.select_form('form[action="https://elearning.mercubuana.ac.id/login/index.php?authldap_skipntlmsso=1"]') # Login Form Elearning URL

file_obj = open("./credentials.json", "r") # Load Nomor Induk Mahasiswa (NIM) and Password

data = json.loads(file_obj.read()) # Load JSON object stored in credentials.json

### Using NIM and Password for login to the elearning
browser["username"] = data['username'] 
browser["password"] = data['password']

### Call submit form to authententicate an user
response = browser.submit_selected()
#page = browser.get_current_page()
matkulURL = browser.links("https://elearning.mercubuana.ac.id/course/view.php")

url_arr = [] # store each matkul URL on this array

# Looping for scanning on each matkul URL
for link in matkulURL:
    browser.follow_link(link)
    url_arr.append(browser.get_url())

def modul_details(input_from_user):
    modul_url = url_arr[input_from_user-1]
    browser.open(modul_url)
    matkul_page = browser.get_current_page().find_all("span", {"class":"instancename"})
    
    print(browser.get_current_page().title.text)
    for i in matkul_page:
        print(i.text.strip())

def home():
    print("List mata kuliah: ")
    for i in url_arr:
        #url = url_arr[i]
        browser.open(i)
        number = url_arr.index(i) + 1
        print(number, ".", browser.get_current_page().title.text)
    input_user = input("Masukkan mata kuliah yang diinginkan: ")
    
    # call to function that collect weekly modul on each matkul
    modul_details(int(input_user))

home()
