class dog:

    def __init__(self, smell="stinky") -> None:
        self._smell = smell


    def rekni(comarict="nemam co rict"):
        return f"pes rika {comarict}"
    def __str__(self) -> str:
        return "jsem pes"
    def __eq__(self, _value: object) -> bool:
        return False if _value<5 else True


    @property
    def smell(self):
        return self._smell
    @smell.setter
    def smell(self, value): #setter/mutator
        """
        sets the value of smell to [value]. either stinky or good
        """
        self._smell = "stinky" if value > 5 else "good :)"
def ffff():
    ...
    # grr = dog()
    # print(dog.rekni("prd"))
    # print(dog())
    # print(grr==2)
    # print(grr.smell)
    # grr.smell = 4
    # print(grr.smell)
class Sheet:

    def __init__(self, height: int, width: int, weight: int) -> None:
        """
        creates a new instance of a sheet of paper

        !!height>=width!!
        :param height: height in mm
        :param width: width in mm
        :param weight: weight of 1m^2 of paper
        """
        assert height >= width, "Height is less than width"
        self._height = height
        self._width = weight
        self._weight = weight

    def halve(self) -> "Sheet":
        """
        cutting in half by height
        :return: new sheet
        """
        return Sheet(self._width, self._height // 2, self._weight)
    def sheet_weight(self) -> float:
        return self._weight * self._height * self._width / 1e6

    def __repr__(self) -> str:
        return f"h: {self._height}, w: {self._width}, weight per 1m^2 {self._weight}"

class Datum:
    def __init__(self, rok, mesic=None, tyden=None, den=None):
        #TODO: assert
        self.rok = rok
        self.mesic = mesic
        self.tyden = tyden
        self.den = den
    def __repr__(self) -> str:
        if self.mesic is None:
            return f"{self.rok}"
        elif self.tyden is None:
            return f"{self.rok}.{self.mesic}"
        elif self.den is None:
            return f"{self.rok}.{self.mesic}.{self.tyden}"
        else:
            return f"{self.rok}.{self.mesic}.{self.tyden}.{self.den}"
        
    # def __str__(self) -> str:
        
    #     return ".".join([str(n) for n in [self.rok, self.mesic,self.tyden, self.den] if n is not None])

    @staticmethod
    def from_repr(rstr) -> "Datum":
        pass     
    @staticmethod
    def prunik(interval1: tuple["Datum", "Datum"], interval2: tuple["Datum","Datum"]):
        pass
    def day_from_epoch(self) -> tuple[int, int]:
        pass

class Postava:
    def __init__(self, name:str, birth:Datum, *, prezdivka:str=None, umrti:Datum=None):
        pass
    @staticmethod
    def from_dict(json_dict: dict) -> "Postava":
        pass

    def to_dict(self) -> dict:
        pass

    def event(self, udalost: "Udalost"):
        pass
    def __repr__(self) -> str:
        pass
    def get_events(self, from_date: Datum, to_date: Datum) -> list["Udalost"]:
        pass

class Udalost:
    def __init__(self,  from_date: Datum, to_date: Datum, desc: str, *,lokace:str= None):
        pass
    @staticmethod
    def from_dict(json_dict) -> "Udalost":
        pass
    def to_dict(self) -> dict:
        pass

from typing import Any

class LinkedDeque:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def __bool__(self):
        return bool(self._size)
    def prepend(self, item):
        self._head = Node(item, self._head)
        if not self:
            self._tail = self._head
        self._size +=1
    def append(self, item):
        og_tail = self._tail
        self._tail = Node(item, None)
        og_tail._next = self._tail
        self._size +=1
        if not self:
            self._head = self._tail
        else:
            og_tail._next = self._tail
    def remove_head(self):
        if not self:
            raise ValueError("smrdis")
        self._head = self._head._next
        self._size -=1
        if not self:
            assert self._head is None
            self._tail = None
    def remove_tail(self):
        ...
        #TODO

    @property
    def head(self):
        if not self:
            raise ValueError("smrdis")
        return self._head._item
    @property
    def tail(self):
        if not self:
            raise ValueError("smrdis")
        return self._tail._item
    def __iter__(self):
        return LinkedDequeIter(self)
    def __len__(self):
        return self._size
    def __str__(self) -> str:
        rls = [f"Len={len(self)}. "]
        if not self:
            rls.append(f"Head:{self._head}, Tail:{self._tail}")
        else:
            node = self._head
            while node:
                if node == self._head:
                    rls.append("Head:")
                if node == self._tail:
                    rls.append("Tail:")
                rls.append(f"{node._item} -> ")
                node = node._next
            else:
                rls.append(" None")
        return "".join(rls)

class LinkedDequeIter:
    def __init__(self, lst:LinkedDeque):
        self._node = lst._head 
    def __next__(self):
        if self._node is None:
            raise StopIteration()
        item = self._node._item
        self._node = self._node._next
        return item

class Node:
    def __init__(self, item:Any, next:"Node"):
        self._item = item
        self._next = next

class A:
    def __init__(self,data) -> None:
        self.data = data

    def print(self):
        print(self.data)


class B(A):
    def __init__(self, data, desription) -> None:
        super().__init__(data)
        self.desription = desription
    def get_presription(self):
        return self.desription
    def print(self):
        print(f"{self.data} {self.desription}")
#spojove strukture: uzly (nesou data) a jsou propojeny
    # + flexibilita
    # - pamet


if __name__ == "__main__":
    # ldq = LinkedDeque()
    # ldq.prepend(2)
    # ldq.prepend(1)
    # ldq.append(3)
    # ldq.append(4)
    # ldq.remove_head()
    # print(list(ldq))
    # print(ldq)
    d = B(8, "moje oblibena")
    d.print()
    # d = Datum(1572,5,6,7)
    # print(f"{repr(d)}, {str(d)}")
# s = Sheet(125, 80, 80)
# print(s)