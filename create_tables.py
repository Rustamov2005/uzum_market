from database import Database


class create():

    @staticmethod
    def create():
        query = f"""CREATE TABLE users(id SERIAL PRIMARY KEY, username VARCHAR(100), password BIGINT); """
        print(Database.connect(query, 'create'))
        print("Muvofaqqiyatli bajarilgan ish!!!")


    @staticmethod
    def insert():
        username = input("foydalanuvchu usenameni kiriting>>>")
        password = input("Foydalanuvchi passwordini kiriting>>>")
        query = f"""INSERT INTO users(username, password) VALUES('{username}', '{password}')"""
        Database.connect(query, 'insert')
        print("Siz muvofaqqiyatli ro'yxatdan o'tdingiz!!!")


    @staticmethod
    def oziq_ovqat():
        query = f"""CREATE TABLE oziq_ovqat(id SERIAL PRIMARY KEY , name VARCHAR(100), narxi NUMERIC);"""
        print(Database.connect(query, 'create'))


    @staticmethod
    def insert_oziq():
        name = input("Oziq ovqat nomini kiriting:")
        narxi = input("Oziq ovqat narxini kiriting:")
        query = f"""INSERT INTO oziq_ovqat(name, narxi) VALUES('{name}', {narxi});"""
        print((Database.connect(query, 'insert')))

    @staticmethod
    def select_oziq():
        query = f"""SELECT * FROM oziq_ovqat;"""
        return Database.connect(query, 'select')

    @staticmethod
    def kiyim():
        query = f"""CREATE TABLE kiyim(id SERIAL PRIMARY KEY, name VARCHAR(100), narx NUMERIC);"""
        Database.connect(query, 'create')

    @staticmethod
    def insert_kiyim():
        name = input("Kiyim nomini kiriting:")
        narx = input("Kiyim narxini kiriting:")
        query = f"""INSERT INTO kiyim(name, narx) VALUES('{name}', {narx} );"""
        print(Database.connect(query, 'insert'))


    @staticmethod
    def kiyim_select():
        query = f"""SELECT * FROM kiyim;"""
        return Database.connect(query, 'select')


if __name__ == "__main__":
    create.insert()
