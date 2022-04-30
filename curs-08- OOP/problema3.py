class CatalogAuto:
    def __init__(self, marca, tip):
        self.marca = marca
        self.tip = tip

    def schimb_culoare(self, culoare):
        self.culoare = culoare

    def __str__(self):
        return f"Culoarea este: {self.culoare}."


class ScauneIncalzite(CatalogAuto):
    def __init__(self, scaune_incalzite, marca, tip):
        super().__init__(marca, tip)
        self.scaune_incalzite = scaune_incalzite

    def __str__(self):
        return f"Marca este: {self.marca}\n \tTipul este: {self.tip}\n \tScaune incalzite: {self.scaune_incalzite}"

class BlocuriOpticeLed(CatalogAuto):
    def __init__(self, blocuri_optice_led, marca, tip):
        super().__init__(marca, tip)
        self.blocuri_optice_led = blocuri_optice_led

    def __str__(self):
        return f"Marca este: {self.marca}\n \t Tipul este: {self.tip}\n \t Blocuri optice: {self.blocuri_optice_led}"

obj = ScauneIncalzite(marca= "ARO", tip= 461, scaune_incalzite= "NU")
print(obj)
obj.schimb_culoare("rosu")
print(obj.culoare)

obj2 = BlocuriOpticeLed(marca="Dacia", tip= 1310, blocuri_optice_led="Nu" )
print(obj2)
obj2.schimb_culoare("negru")
print(obj2.culoare)
print(obj2.culoare, obj2.blocuri_optice_led, obj2.marca, obj2.tip)
print(obj.culoare, obj.scaune_incalzite, obj.marca, obj.tip)