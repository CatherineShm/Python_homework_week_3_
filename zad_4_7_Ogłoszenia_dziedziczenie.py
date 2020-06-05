# ### Zadanie 4.7 | Ogłoszenia / dziedziczenie
# Do zadania z klasą `Ogloszenie` dodaj kolejne kolejne klasy, które po niej dziedziczą.
# `OgloszenieSamochodowe` – dziedziczy z `Ogloszenie` i dodatkowo określa cechy sprzedawanego
# samochodu jak model, markę, rok produkcji, przebieg, pojemność, moc i rodzaj paliwa.
# `OgloszenieMieszkaniowe` – też dziedziczy z `Ogloszenie`, a dodatkowo cechy sprzedawanego
# mieszkania / domu: miejscowość, metraż, liczba pokoi.

from zad_4_1_Ogłoszenia import Advertissement



class Cars_advertissement(Advertissement):
    def __init__(self,objective, subject, description, price, vendors_name, phone,
                 model, brand, productions_year, mileage, engine_power):
        super().__init__(objective, subject, description, price, vendors_name, phone)
        self.model = model
        self.brand = brand
        self.productions_year = productions_year
        self.mileage = mileage
        self.engine_power = engine_power


    def details(self):
        return f"---> Model: {self.model}\n" \
               f"---> Brand: {self.brand}\n" \
               f"---> Productions_year: {self.productions_year}\n" \
               f"---> Mileage: {self.mileage}\n" \
               f"---> Engine_power: {self.engine_power}"


class Housing_ads(Advertissement):
    def __init__(self, objective, subject, description, price, vendors_name, phone,
                 locality, area, pieces):
        super().__init__(objective, subject, description, price, vendors_name, phone)
        self.locality = locality
        self.area = area
        self.pieces = pieces


    def details(self):
        return f"---> Miejscowość: {self.locality}\n" \
               f"---> Metraż: {self.area}\n" \
               f"---> Liczba pokoi: {self.pieces}"


car = Cars_advertissement("na sprzedaż", "samochów", "w bardzo dobtym stanie",45000, "Jan", 222333666, "X5", "BMW", 2015, 95000, 500)
print(car.get_info())
print(car.details())

flat = Housing_ads("na wynajem", "mieszkanie", "jasne, przestrzenne; parter", "3500 zł", "Ala", 444555666, "Warszawa, Szmulowizna", "40 m²", "2 pokoje")
print(flat)
print(flat.details())