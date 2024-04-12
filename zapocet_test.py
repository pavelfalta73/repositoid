class Lanovka:
    def __init__(self, kapacita, max_pocet_bezporuchy_jizd, pocet_jizd=1, pasazeri = list()):        
        self._pasazeri = pasazeri
        self._kapacita = kapacita
        self._pocet_jizd = pocet_jizd
        self._max_pocet_bezporuchy_jizd = max_pocet_bezporuchy_jizd
        self._dojezd = list()

    def pridat(self, pasazer):
        self._pasazeri.append(pasazer)

    def zacni(self):
        self.vyjed()

    def vyjed(self):
        pasazeri = self._pasazeri
        pocet_jizd = ceil(len(pasazeri) / self._kapacita)

        if debug:
            print(f"pocet_jizd_pred_nama {pocet_jizd}")
        
        for _ in range(pocet_jizd):
            self.vyhodnotit_pad([pasazeri.pop(0) for _ in range(self._kapacita) if pasazeri])

    def vyhodnotit_pad(self, pasazeri):
        if self._pocet_jizd>=self._max_pocet_bezporuchy_jizd and randint(0,10-self._pocet_jizd) == 0:
            print(f"{[pas.jmeno for pas in pasazeri]} ZEMRELI V PADU LANOVKY HASHAHSHSHAHHAAG <3")
            self._pocet_jizd = 1
        else:
            if debug:
                print("")
                print(f"jizda c. {self._pocet_jizd}")

            self._pocet_jizd +=1
            self.vystoupit(pasazeri)
    
    def vystoupit(self, pasazeri):
        pasazeri_venku = [pasazeri.pop() for _ in range(len(pasazeri))]

        if debug:
            print(f"pasazeri {pasazeri_venku} vystoupili")

        self.bludiste(pasazeri_venku)
    
    def bludiste(self, pasazeri):
        promichat = [pasazeri.pop(randrange(len(pasazeri))) for _ in range(len(pasazeri))]
        
        if debug:
            print(f"pasazeri {promichat} se promichali")

        self.dojezd(promichat)

    def dojezd(self, pasazeri):
        [self._dojezd.append(pasazeri.pop()) for _ in range(len(pasazeri))]
        
        

    @property
    def dojezd_vrat(self):
        return self._dojezd

class Prodejce:
    def __init__(self, nalada, cena_za_jizdu):
        self._nalada = nalada
        self._cena_za_jizdu = cena_za_jizdu

    @property
    def nalada(self):
        return self._nalada
    @nalada.setter
    def nalada(self, val):
        self._nalada == val

class Pasazer:
    def __init__(self, jmeno, vek, finance):
        self._jmeno = jmeno
        self._finance = finance
        self._vek = vek

    def koupit_listek(self):
        if prodejce.nalada>=9 and randint(0,3) == 1:
            if debug:
                print(f"pasazer {pasazer} ma jizdu zdarma")
            lanovka.pridat(pasazer)
        elif pasazer.finance >= 100:
            pasazer.finance -= 100
            if debug:
                print(f"pasazer {pasazer} si jizdu zaplatil")
            lanovka.pridat(pasazer)
        else:
            if debug:
                print(f"pasazer {pasazer} nemel na jizdu")
                pasazeri.remove(pasazer)
        if debug:
            print("")

    def __repr__(self) -> str:
        return repr(f"jmeno:{self.jmeno}, vek: {self.vek}, finance: {self.finance}")
    
    @property
    def jmeno(self):
        return self._jmeno
    @property
    def vek(self):
        return self._vek
    @property
    def finance(self):
        return self._finance
    @finance.setter
    def finance(self, castka):
        self._finance = castka

class Policie:
    def __init__(self, jmeno_hledane_osoby, vek_hledane_osoby):
        self._jmeno_hledane_osoby = jmeno_hledane_osoby
        self._vek_hledane_osoby = vek_hledane_osoby
        self._chyceno = False

    def prosetri(self, seznam):
        seradit = self.serad_podle_veku(seznam)
        if debug:
            print("")
            print(f"pasazeri {seradit} se seradili pomoci quicksortu, a jdou prohledani")
        if self._vek_hledane_osoby < 40:
            podezrely = ([_ for _ in seradit if _.vek == self._vek_hledane_osoby and _.jmeno == self._jmeno_hledane_osoby])
            if podezrely:
                print("")
                print(f"pasazer {podezrely} byl dopaden!")
                self.chyceno = True
        else:
            podezrely = ([_ for _ in reversed(seradit) if _.vek == self._vek_hledane_osoby and _.jmeno == self._jmeno_hledane_osoby])
            if podezrely:
                print("")
                print(f"pasazer {podezrely} byl dopaden!")
                self.chyceno = True

    def serad_podle_veku(self, seznam): #quicksort implementaci, kterou jsem napsal z hlavy a na kterou jsem pysnej
        if len(seznam) < 2: return seznam
        pivot = seznam.pop()
        return self.serad_podle_veku([mensi for mensi in [pas for pas in seznam] if mensi.vek <= pivot.vek]) + [pivot] + self.serad_podle_veku([vetsi for vetsi in [pas for pas in seznam] if vetsi.vek > pivot.vek])
    @property
    def chyceno(self):
        return self._chyceno
        
    @chyceno.setter
    def chyceno(self, val):
        self._chyceno = val

def generuj_pasazery(n,vek=(0,99),finance=(0,999)):
    return [Pasazer(get_first_name(), randint(vek[0],vek[1]), randint(finance[0],finance[1])) for i in range(n)]

if __name__ == "__main__":
    from random import randint, randrange, choice
    from names import get_first_name
    from math import ceil

    global debug
    debug = True #######SWITCH OUTPUTU (jo ja vim global bleh) True zapne printy

    policie = Policie(jmeno_hledane_osoby="John", vek_hledane_osoby=69) #definice objektu policie, koho hleda
    prodejce = Prodejce(nalada=9, cena_za_jizdu=100)
    lanovka = Lanovka(kapacita=2,max_pocet_bezporuchy_jizd=2)

    while not policie.chyceno: #smycka dokud nechyti podezreleho

        pasazeri = list()
        pasazeri.append(Pasazer(jmeno="John",vek=69,finance=101)) #kdyz chceme plantnout krimimalnika
        pasazeri.extend(generuj_pasazery(50)) #generovani n pasazeru s tuple argumentama vek(min, max) a finance(min, max)

        for pasazer in pasazeri:
            pasazer.koupit_listek() #kupovani listku
        else:
            lanovka.zacni() #lanovka vyjizdi
            if debug:
                print("")
                print(f"pasazeri {lanovka.dojezd_vrat} se znovu spojili, a ceka na ne policie")
            policie.prosetri(lanovka.dojezd_vrat) #policie setri
    else:
        if debug:
            print("policie dopadla kriminalnika")