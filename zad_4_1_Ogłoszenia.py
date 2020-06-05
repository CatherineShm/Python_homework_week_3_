# ## 4. Klasy
# ### Zadanie 4.1 | Ogłoszenia
# Zaproponuj klasę, w której obiektach będzie się zapisywać ogłoszenia (takie jak w serwisie internetowym z ogłoszeniami).
# Najlepiej, aby klasa `Ogloszenie` opisywała rzeczy, które posiada każde ogłoszenie, m.in. tytuł, opis, cenę,
# dane kontaktowe sprzedawcy.
from abc import abstractmethod


class Advertissement:
    def __init__(self,objective, subject, description, price, vendors_name, phone):
        """
        This function get the data about the subject of the advertissement.
        :param objective:
        :param subject:
        :param description:
        :param price:
        :param vendors_name:
        :param phone:
        """
        self.objective = objective
        self.subject = subject
        self.description = description
        self.price = price
        self.vendors_name = vendors_name
        self.phone = phone


    def get_info(self) -> str:
        return (f"-> Cel: {self.objective}\n"
                f"-> Temat ogłoszenia: {self.subject}\n"
                f"-> Opis: {self.description}\n"
                f"-> Cena: {self.price}\n"
                f"-> Sprzedający: {self.vendors_name}, tel.: {self.phone}")

    def print_info(self):
        print(self.get_info())

    def __str__(self):
        return self.get_info()


    @abstractmethod
    def details(self):
        pass