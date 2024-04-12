class list_extremu:
    def __init__(self, seznam, size):
        self._seznam = seznam
        self._size = size
        self._extremy = list()

    def napln(self, prvek):
        if len(self._extremy) < self._size:
            self._extremy.append(prvek)
        else:
            self.nahrad_nejmensi(prvek)

    def nahrad_nejmensi(self, prvek):
        self._extremy = sorted(self._extremy)
        if self._extremy[0] < prvek:
                self._extremy[0] = prvek

    def __repr__(self) -> str:
        return repr(self._extremy)

class opak:
    def __init__(self, seznam, pocet_opak):
        self._seznam = seznam
        self._pocet_opak = pocet_opak

    def vrat_hrisniky(self) -> list:
        hrisnici = list()
        count = 0
        self._seznam = sorted(self._seznam)

        for i in range(len(self._seznam)-1):

            if count < self._pocet_opak:
                if self._seznam[i] == self._seznam[i+1]:

                    count +=1
                else:
                    count = 0
            else:
                hrisnici.append(self._seznam[i])

        return list(set(hrisnici))
                


def najit_k_max(seznam, k):

    le = list_extremu(seznam, k)

    for prvek in seznam:
        le.napln(prvek)

    return le


def indexran(seznam, prvek):
    from time import process_time
    from random import randrange
    start = process_time()
    while True:
        i = randrange(len(seznam))
        if seznam[i] == prvek:
            stop = process_time()
            return i, stop-start
        elif process_time()-start:
            return None

def disekce(seznam, prvek):
    pivot = len(seznam) // 2
    seznam = sorted(seznam)


    while seznam[pivot] != prvek:
        if len(seznam) == 1:
            return False
        elif seznam[pivot] > prvek:
            seznam = seznam[:pivot]

            pivot = len(seznam) // 2
        else:
            seznam = seznam[pivot:]

            pivot = len(seznam) // 2
    else:
        return True



test_hrisnici = opak([2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,8], 2)
#print(test_hrisnici.vrat_hrisniky())

print(indexran([2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,
                3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,
                1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,
                8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,33,2,5,8,4,
                5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,
                7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,
                7,8,8,6564,4648,48,48,48,48,48484561,8,98,64,8789,
                5,15,87,84,51,6,88,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,
                3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,
                1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,
                8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,33,2,5,8,4,
                5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,
                7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,
                7,8,8,6564,4648,48,48,48,48,48484561,8,98,64,8789,
                5,15,87,84,51,6,88,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,
                3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,
                1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,
                8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,33,2,5,8,4,
                5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,
                7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,
                7,8,8,6564,4648,48,48,48,48,48484561,8,98,64,8789,
                5,15,87,84,51,6,88,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,
                3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,
                1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,
                8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,33,2,5,8,4,
                5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,
                7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,
                7,8,8,6564,4648,48,48,48,48,48484561,8,98,64,8789,
                5,15,87,84,51,6,88,47], 47))



#print(index_chytre([2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,8], 3))
#print(disekce([2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,8,2,5,8,4,5,6,3,1,4,9,7,5,1,5,6,6,7,8,8], 13))
#print(najit_k_max([1,5,7,6,9,1,2,6,3], 3))