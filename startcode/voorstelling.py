class Voorstelling:

    def __init__(self, naam, aantal_plaatsen):
        self.__naam = naam
        self.__aantal_plaatsen = aantal_plaatsen
        self.__aantal_verkocht = 0

    def get_naam(self):
        return self.__naam

    def get_aantal_plaatsen(self):
        return self.__aantal_plaatsen

    def get_aantal_verkocht(self):
        return self.__aantal_verkocht
    
    def verkoop_kaartje(self):
        if self.__aantal_plaatsen > 0:
            self.__aantal_plaatsen -= 1
            self.__aantal_verkocht += 1