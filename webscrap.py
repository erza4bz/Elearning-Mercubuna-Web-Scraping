import mechanicalsoup
import getpass

def rpl():
    RPL = "https://elearning.mercubuana.ac.id/course/view.php?id=6040" #sesuaikan dengan matkul
    rpl_page = browser.get(RPL)
    materi_rpl = rpl_page.soup.findAll("span", {"class":"instancename"})
    for i in materi_rpl:
        print(i.text.strip())
    return show_menu()

def ai():
    AI = "https://elearning.mercubuana.ac.id/course/view.php?id=6412" #sesuaikan dengan matkul
    ai_page = browser.get(AI)
    materi_ai = ai_page.soup.findAll("span", {"class":"instancename"})
    for i in materi_ai:
        print(i.text.strip())
    return show_menu()

def so():
    SO = "https://elearning.mercubuana.ac.id/course/view.php?id=6041" #sesuaikan dengan matkul
    so_page = browser.get(SO)
    materi_so = so_page.soup.findAll("span", {"class":"instancename"})
    for i in materi_so:
        print(i.text.strip())
    return show_menu()

def show_menu():
    print("\n")
    print("-----------MATA KULIAH-----------")
    print("[1] KECERDASAN BUATAN")
    print("[2] SISTEM OPERASI")
    print("[3] REKAYASA PERANGKAL LUNAK")
    print("[0] EXIT")
    menu = input("Pilih Matkul: ")
    print("\n")

    if menu == "1":
        ai()
    elif menu == "2":
        so()
    elif menu == "3":
        rpl()
    elif menu == "0":
        print("See ya!")
        exit()
    else:
        print("Pilih yang bener!")
        return show_menu()
if __name__ == "__main__":

    URL = "https://elearning.mercubuana.ac.id"
    NIM = input("Masukkan NIM: ")
    PASS = getpass.getpass()

    browser = mechanicalsoup.Browser()
    login_page = browser.get(URL)

    login_form = login_page.soup.find("form", {"class":"navbar-form pull-right"})
    #print(login_form.prettify()) //print response
    login_form.find("input", {"name":"username"}) ["value"] = NIM
    login_form.find("input", {"name":"password"}) ["value"] = PASS

    response = browser.submit(login_form, login_page.url)
    if response.soup.find("span",{"itemprop":"title"}):
        show_menu()
    else:
        print("Mungkin NIM dan Password tidak sesuai")