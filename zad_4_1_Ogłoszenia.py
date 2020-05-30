# ## 4. Klasy
# ### Zadanie 4.1 | Ogłoszenia
# Zaproponuj klasę, w której obiektach będzie się zapisywać ogłoszenia (takie jak w serwisie internetowym z ogłoszeniami).
# Najlepiej, aby klasa `Ogloszenie` opisywała rzeczy, które posiada każde ogłoszenie, m.in. tytuł, opis, cenę,
# dane kontaktowe sprzedawcy.

class Advertissement:
    def __init__(self,objective, object, description, price, vendors_name, phone):
        self.objective = objective
        self.object = object
        self.description = description
        self.price = price
        self.vendors_name = vendors_name
        self.phone = phone


    def get_info(self) -> str:
        return (f"-> Cel: {self.objective}\n"
                f"-> Temat ogłoszenia: {self.object}\n"
                f"-> Opis: {self.description}\n"
                f"-> Cena: {self.price}\n"
                f"-> Sprzedający: {self.vendors_name}, tel.: {self.phone}")

    def print_info(self):
        print(self.get_info())

    def __str__(self):
        return self.get_info()

advert_1 = Advertissement("sprzedaż", "samochód", "używany, w dobrym stanie", "5000 zl", "Jan", "222 333 444")
advert_1.print_info()