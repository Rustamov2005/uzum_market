import user_page
from create_tables import create
import admin_page


def login():
    print("login page:")
    username = input("Yusernamingizni kiriting:")
    password = input("Passwordingizni kiriting:")
    idsi = input("foydalanuvchi id sini kiriting:")
    if idsi == "2":
        query = f"""SELECT * FROM users WHERE username='{username}' and password ={password};"""
        if query:
            return admin_page.admin()
        else:
            print("Bunday foydalanuvchi mavjud emas!!!")
            return uzum()
    else:
        print("User page xush kelibsiz>>>")
        return user_page.user()


def regester():
    print("Regester page:")
    return create.insert()


def uzum():
    uzum_2 = input("""
    Uzumning vebsaytiga xush kelibsiz:
        1.login
        2.regester
         >>>""")
    if uzum_2 == "1":
        return login()

    elif uzum_2 == "2":
        return regester()

    else:
        print("Bunday xizmat ruti mavjud emas!!!")
        return uzum()


if __name__ == "__main__":
    uzum()