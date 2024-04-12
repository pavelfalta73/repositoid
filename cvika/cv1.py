class Pes:
    
    #initor/inicializer/konstruktor
    def __init__(self,jmeno,vek,majitele):
        self._jmeno = jmeno
        self._vek = vek
        self._majitele = majitele

    #property/vlastnosti
    @property
    def jmeno(self): #getter/accesor
        return "Haf haf " + self._jmeno + " vrrr haf"
    @jmeno.setter
    def jmeno(self, value): #setter/mutator
        self._jmeno = value if len(value) > 3 else self._jmeno

    def curej(self, na_koho): #operace/metody
        print(f"Pes {self.jmeno} cura na {na_koho}")

    #magicke metody (pretezovani operatoru)
    def __ge__(self, other): #self >= other -> p1 = self.__ge__(p1, other)
        return self._vek >= other.vek


def main():
    p1 = Pes(jmeno="Azor", vek=5, majitele=["Petr","Jana"])
    p2 = Pes(jmeno="Rex", vek=3, majitele=["Jachym"])
    print(p1.jmeno)

    p1.jmeno = "Fique"
    print(p1.jmeno)
    print(p1 >= p2)

main()