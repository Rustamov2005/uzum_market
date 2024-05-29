from create_tables import create
from database import Database
import admin_page
import first_page


class electron():

     @staticmethod
     def create_electron():
        query = f"""CREATE TABLE electronika(id SERIAL PRIMARY KEY, name VARCHAR(100), narxi VARCHAR(100));"""
        print(Database.connect(query, 'create'))

     @staticmethod
     def insert_electron():
        name = input('Name: ')
        narxi = input('Narxi: ')
        query = f"""INSERT INTO electronika (name, narxi) VALUES ('{name}', '{narxi}');"""
        print(Database.connect(query, 'insert'))

     @staticmethod
     def select_electron():
        query = f"""SELECT * FROM electronika;"""
        print(Database.connect(query, 'select'))


class uy_jihoz():

    @staticmethod
    def select_uy_jihoz():
        query = f"""SELECT * FROM uy_jihoz;"""
        print(Database.connect(query, 'select'))

    @staticmethod
    def insert_uy_jihoz():
        name = input('Name: ')
        narxi = input('Narxi: ')
        query = f"""INSERT INTO uy_jihoz(name, narxi) VALUES('{name}', '{narxi}')"""
        print(Database.connect(query, 'insert'))

    @staticmethod
    def create_uy_jihoz():
        query = f"""CREATE TABLE uy_jihoz(id SERIAL PRIMARY KEY, name VARCHAR(100), narxi VARCHAR(100));"""
        print(Database.connect(query, 'create'))


def maxsulotlar():
    maxsulot = input("""
    Maxsulotlar toifalari:
        1.Oziq-ovqat.
        2.Kiyim-kechaklar.
        3.Elektron - qurilmalar.
        4.uy_jihozlari
        5.back
          >>>""")
    if maxsulot == "1":
        print(create.select_oziq())
        return maxsulotlar()
    elif maxsulot == "2":
        print(create.kiyim_select())
        return maxsulotlar()
    elif maxsulot == "3":
        print(electron.select_electron())
        return maxsulotlar()
    elif maxsulot == "4":
        print(uy_jihoz.select_uy_jihoz())
        return maxsulotlar()
    elif maxsulot == "5":
        return shop()


class new_product():

    @staticmethod
    def yangi_maxsulotlar():
        query = f"""CREATE TABLE ne_product(id SERIAL PRIMARY KEY, name VARCHAR(100), narxi VARCHAR(100));"""
        Database.connect(query, 'create')
        print("Table yaratildi:")

    @staticmethod
    def select_new_product():
        query = f"""SELECT * FROM ne_product;"""
        print(Database.connect(query, 'select'))

    @staticmethod
    def insert_new_product():
        name = input("Enter new product name: ")
        narxi = input("Enter new product price: ")
        query = f"""INSERT INTO ne_product(name, narxi) VALUES ('{name}', '{narxi}');"""
        Database.connect(query, 'insert')


class chegirma():

    @staticmethod
    def chegirmalar():
        query = f"""SELECT * FROM chegirma;"""
        print(Database.connect(query, 'select'))

    @staticmethod
    def insert_chegirma():
        name = input("Enter new chegirma name: ")
        narxi = input("Enter new chegirma price: ")
        query = f"""INSERT INTO chegirma(name, narxi) VALUES ('{name}', '{narxi}');"""
        Database.connect(query, 'insert')

    @staticmethod
    def create_chegirma():
        query = f"""CREATE TABLE chegirma(id SERIAL PRIMARY KEY, name VARCHAR(100), narxi VARCHAR(100));"""
        Database.connect(query, 'create')


def eng_kop():
    query = f"""SELECT * FROM product;"""
    print(Database.connect(query, 'select'))


def shop():

    print("Shopping page ga xush kelibsiz!!!")
    serveses = input("""
        Xizmat turini tanlang:
            1.maxsulot toifalari.
            2.yangi kelgan maxsulotlar.
            3.chegirmalar va aksiyalar.
            4.eng ko'p sotilayotgan maxsulotlar.
            5.Back
          >>>""")
    if serveses == "1":
        return maxsulotlar()
    elif serveses == "2":
        print(new_product.select_new_product())
        return shop()
    elif serveses == "3":
        print(chegirma.chegirmalar())
        return shop()
    elif serveses == "4":
        print(eng_kop())
        return shop()
    elif serveses == "5":
        return user()

    else:
        print("Siz noto'g'ri tugmani tanladingiz qayta urinib ko'ring!!!")
        return user()


class Cardsr:

    @staticmethod
    def cards_select():
        query = f"""SELECT * FROM cards;"""
        print(Database.connect(query, 'select'))


    @staticmethod
    def create_cards():
        query = f"""CREATE TABLE cards(id SERIAL PRIMARY KEY, card_number VARCHAR(16), card_date DATE, name VARCHAR(20));"""
        print(Database.connect(query, 'create'))


    @staticmethod
    def cards_insert():
        card_number = input("Enter your card number:")
        card_date = input("Enter your card date:")
        card_name = input("Enter your card name:")
        query = f"""INSERT INTO cards(card_number, card_date, name) VALUES ('{card_number}','{card_date}','{card_name}')"""
        Database.connect(query, 'insert')
        print("Your card has been added successfully>>>")


def cards():
    serveses = input("""
        1.Kaetalarni ko'rish
        2.Karta qo'shish
        3.Back
           >>>""")
    if serveses == "1":
        print(Cardsr.cards_select())
        return cards()
    elif serveses == "2":
        print(Cardsr.cards_insert())
        return cards()
    elif serveses == "3":
        return user()
    else:
        print("Siz xato tugmani tanladingiz:")
        return cards()


def accaunt():
    story = input("""
        Xizmat turini tanlang:
            1.story
            2.cards
            3.back
          >>>""")
    if story == "1":
        print(eng_kop())
        return accaunt()
    elif story == "2":
        print(Cardsr.cards_select())
        return accaunt()
    elif story == "3":
        return user()


def user():
    # print("Yuers gage:")
    serveses = input("""
        xizmatlar ro'yxati:
            1.shopping
            2.accaunt
            3.cards
            4. back
            5.search
          >>>""")
    if serveses == "1":
        return shop()
    elif serveses == "2":
        return accaunt()
    elif serveses == "3":
        return cards()
    elif serveses == "4":
        return admin_page.admin()
    elif serveses == "5":
        print(search())
        return user()
    else:
        print("Siz xato tugmani tanladingiz:")
        return user()


def search():
    name = input("Enter your product name:")
    query = f"""SELECT * FROM product WHERE name LIKE '%{name}%';"""
    print(Database.connect(query, 'select'))



# if __name__ == "__main__":
#     uy_jihoz.insert_uy_jihoz()
