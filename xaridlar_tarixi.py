from database import Database


class xaridlar_tarixi():
    def __init__(self, name: str, narxi: int, date: str):
        self.name = name
        self.narxi = narxi
        self.date = date


    @staticmethod
    def xaridlar(name, narxi, date):
        query = f"""INSERT INTO xaridlar(name, narxi, date) VALUES ('{name}', '{narxi}', '{date}');"""


    def __str__(self):
        return f"{self.name}  {self.narxi}  {self.date}"


Buy = xaridlar_tarixi("sumka", 100000, "2022-01-04")
print(Buy)


