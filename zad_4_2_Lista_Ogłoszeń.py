# ### Zadanie 4.2 | Lista ogłoszeń
# Napisz programy, w których tworzysz listę ogłoszeń samochodowych, a następnie wyszukujesz
# ogłoszenia na podstawie ich parametrów.
# Na przykład ogłoszenia o cenach z określonego przedziału.
# Użyj funkcji `lambda`, określających, które ogłoszenia powinny zostać wyszukane.
# Użyj poznanych kolekcji do trzymania ogłoszeń. Możesz zastosować metodę `filter`
# do wyszukiwania odpowiednich ogłoszeń.


class Cars:
    def __init__(self, objective, brand, price, vendor):
        self.objective = objective
        self.brand = brand
        self.price = price
        self.vendor = vendor


    def get_info(self):
        return f"Typ ogłoszenia: {self.objective}\n" \
               f"Marka samochodu: {self.brand}\n" \
               f"Cena: {self.price}\n" \
               f"Sprzedawca: {self.vendor}"


    def __str__(self):
        return self.get_info()

ceny = []
cars = {"car1": {"marka": "BMW", "cena": 5500, "sprzedawca": "Jan K."},
        "car2": {"marka": "Volvo", "cena": 4000, "sprzedawca": "Michał M."},
        "car2": {"marka": "BMW", "cena": 4800, "sprzedawca": "Jurek L."},
        "car2": {"marka": "Volkswagen", "cena": 5000, "sprzedawca": "Lukasz M."},
        "car2": {"marka": "Citroën", "cena": 5300, "sprzedawca": "Mark G."},
        "car2": {"marka": "Citroën", "cena": 6000, "sprzedawca": "Mirek J."},
        "car2": {"marka": "Volvo", "cena": 4700, "sprzedawca": "Grzegorz B."}}


def get_list_what_you_want(dict):
    for car in dict:
        for item in car:
            if item == "cena":
                ceny.append(car["cena"])
                return ceny


get_list_what_you_want(cars)
print(ceny)
