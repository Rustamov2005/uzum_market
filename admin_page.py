# from database import Database
# import user_page
#
#
# class admin_customers():
#
#     @staticmethod
#     def select():
#         query = f"""SELECT * FROM customers;"""
#         print(Database.connect(query, 'select'))
#
#     @staticmethod
#     def insert():
#         first_name = input("Enter yusers first name:")
#         last_name = input("Enter yusers last name:")
#         brith_date = input("Enter yusers brith date::")
#         query = f"""INSERT INTO customers(first_name, last_name, brith_date) VALUES('{first_name}', '{last_name}', '{brith_date}')"""
#         print(Database.connect(query, 'insert'))
#
#     @staticmethod
#     def delete():
#         idsi = input("Enter users id:")
#         query = f"""DELETE FROM customers WHERE id={idsi}"""
#         Database.connect(query, 'delete')
#         print("Deleted user>>>")
#
#     @staticmethod
#     def update_customers():
#         first_name = input("Enter users first name:")
#         last_name = input("Enter users last name:")
#         brith_date = input("Enter users brith  date:")
#         old_name = input("Enter users old name:")
#         query = f"""UPDATE customers SET first_name = '{first_name}', last_name = '{last_name}',
#         brith_date = '{brith_date}' WHERE first_name = '{old_name}'"""
#         Database.connect(query, 'update')
#         print("Updated seccessfull>>>")
#
# class admin_story:
#     @staticmethod
#     def select_story():
#         query = f"""SELECT * FROM story;"""
#         print(Database.connect(query, 'select'))
#         print("Selected seccessfull>>>")
#
#     @staticmethod
#     def insert_story():
#         name = input("Enter stores name:")
#         query = f"""INSERT INTO story(name) VALUES('{name}')"""
#         Database.connect(query, 'insert')
#         print("Inserted seccessfull>>>")
#
#
#     @staticmethod
#     def delete_story():
#         name = input("Enter storys name:")
#         query = f"""DELETE FROM story WHERE name = '{name}'"""
#         Database.connect(query, 'delete')
#         print("Deleted seccessfull>>>")
#
#
#     @staticmethod
#     def update_story():
#         name = input("Enter columns name:")
#         id = input("Enter columns id:")
#         query = f"""UPDATE story SET name = '{name}' WHERE id = {id}"""
#         Database.connect(query,'update')
#         print("Updated seccessfull:")
#
#
# def select():
#     serveses = input("""
#     select the type of service:
#         1.select_customers
#         2.insert_customers
#         3.delete_customers'
#         4.update_customers
#         5.select_story
#         6.insert_story
#         7.delete_story
#         8.update_story
#         9.Back
#             >>> """)
#
#     if serveses == "1":
#         print(admin_customers.select())
#         return select()
#
#     elif serveses == "2":
#         print(admin_customers.insert())
#         return select()
#
#     elif serveses == "3":
#         print(admin_customers.delete())
#         return select()
#
#     elif serveses == "4":
#         print(admin_customers.update_customers())
#         return select()
#
#     elif serveses == "5":
#         print(admin_story.select_story())
#         return select()
#
#     elif serveses == "6":
#         print(admin_story.insert_story())
#         return select()
#
#     elif serveses == "7":
#         print(admin_story.delete_story())
#         return select()
#
#     elif serveses == "8":
#         print(admin_story.update_story())
#         return select()
#     elif serveses == "9":
#         return admin()
#     else:
#         print("siz xato tugmani tanladingiz:")
#         return select()
#
#
# def delete():
#     name = input("Enter Users name:")
#     qyery = f"""DELETE FROM users  WHERE username = '{name}'"""
#     print(Database.connect(qyery, 'delete'))
#     return admin()
#
#
# def admin():
#     serveses = input("""
#         Xizmat turini tanlang:
#             1.select_tables
#             2.users_cards
#             3.accaunt
#             4.delete_user
#            >>>""")
#     if serveses == "1":
#         return select()
#     elif serveses == "2":
#         print(user_page.Cardsr.cards_select())
#         return admin()
#     elif serveses == "3":
#         return user_page.accaunt()
#     elif serveses == "4":
#         return delete()
#
#     else:
#         print("Siz noto'g'ri tugmani tanladingiz:")
#         return admin()
#
#
# # if __name__ == '__main__':
# #     admin()
#
# class admin_name:
#     @staticmethod
#     def akmal():
#         name = input("Enter Users name:")
#
#
class Defsdnfv:
    def __init__(self, name):
        self.name = name
    @property
    def namea(self):
        return self.name


    def __str__(self):
        return self.name

Isim = Defsdnfv("Akmal")
Isim.namea
print(Isim)



