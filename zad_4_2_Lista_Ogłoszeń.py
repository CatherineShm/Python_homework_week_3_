# ### Zadanie 4.2 | Lista ogłoszeń
# Napisz programy, w których tworzysz listę ogłoszeń samochodowych, a następnie wyszukujesz
# ogłoszenia na podstawie ich parametrów.
# Na przykład ogłoszenia o cenach z określonego przedziału.
# Użyj funkcji `lambda`, określających, które ogłoszenia powinny zostać wyszukane.
# Użyj poznanych kolekcji do trzymania ogłoszeń. Możesz zastosować metodę `filter`
# do wyszukiwania odpowiednich ogłoszeń.
x = 0
# class Cars:
#     def __init__(self, objective, brand, price, vendor):
#         self.objective = objective
#         self.brand = brand
#         self.price = price
#         self.vendor = vendor
#     def get_info(self):
#         return f"Typ ogłoszenia: {self.objective}\n" \
#                f"Marka samochodu: {self.brand}\n" \
#                f"Cena: {self.price}\n" \
#                f"Sprzedawca: {self.vendor}"
#     def __str__(self):
#         return self.get_info()
#     def creat_a_tuple(self):
#         all_adv = ()
#         # all_adv += self.__class__
#
# class Advertisements:
#     def __init__(self):
#         self._items = dict()
#
#     def add_advertisement(self, car: Cars):
#         if not isinstance(car, Cars):
#             raise TypeError("This advertisement isn't available.")
#         else:
#             return self.__class__
# car1 = Cars("sprzedaż", "BMW", 5500, "Jan K.")
# car2 = Cars("sprzedaż", "Volvo", 4000, "Michał M.")
# car3 = Cars("sprzedaż", "BMW", 4800, "Jurek L.")
# car4 = Cars("sprzedaż", "Volkswagen", 5000, "Lukasz M.")
# car5 = Cars("sprzedaż", "Citroën", 5300, "Mark G.")
# car6 = Cars("sprzedaż", "Citroën", 6000, "Mirek J.")
# car7 = Cars("sprzedaż", "Volvo", 4700, "Grzegorz B.")
car1 = {"marka": "BMW", "cena": 5500, "sprzedawca": "Jan K."}
car2 = {"marka": "Volvo", "cena": 4000, "sprzedawca": "Michał M."}
car3 = {"marka": "BMW", "cena": 4800, "sprzedawca": "Jurek L."}
car4 = {"marka": "Volkswagen", "cena": 5000, "sprzedawca": "Lukasz M."}
car5 = {"marka": "Citroën", "cena": 5300, "sprzedawca": "Mark G."}
car6 = {"marka": "Citroën", "cena": 6000, "sprzedawca": "Mirek J."}
car7 = {"marka": "Volvo", "cena": 4700, "sprzedawca": "Grzegorz B."}
cars = {}
cars[car1] = {"marka": "BMW", "cena": 5500, "sprzedawca": "Jan K."}

print(cars)


