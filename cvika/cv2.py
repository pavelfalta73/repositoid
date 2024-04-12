from random import randrange

class Queue:
    def __init__(self, fronta=list(), max_pamet=10):
        self._fronta = fronta
        self._max_pamet = max_pamet
        

    def enqueue(self, prvek):
        """
        prida prvek na konec fronty
        :param prvek: prvek na zarazeni
        """
        assert self.size() <= self._max_pamet, f"this queue can only hold {self._max_pamet} items."
        self._fronta.append(prvek)
    
    def dequeue(self):
        return self._fronta.pop(0)
    
    def front(self):
        return self._fronta[0]
    
    def rear(self):
        return self._fronta[-1]
    
    def isEmpty(self):
        return False if self._fronta else True
    
    def size(self):
        return len(self._fronta)

class Stack:
    def __init__(self, items = list()):
        self._items = items

    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        assert not self.isEmpty()
        return self._items.pop()
    
    def peek(self):
        return None if self.isEmpty() else self._items[-1]
    
    def isEmpty(self):
        return not bool(self._items)
        #return False if self._items else True
    
    def size(self):
        return len(self._items)
    
    def __bool__(self):
        return bool(self._items)
    
    def __repr__(self) -> str:
        return repr(self._items)
    
    def __len__ (self):
        return len(self._items)
    
    @property
    def items(self):
        return self._items
    
class ScleroticSet:
    """
    Skleroticke mnoziny maji semantiku mnozin, ale jen omezenou kapacitu.
    Pokud je kapacita vyuzita, nahodne zapominaji vlozene udaje.
    """
    def __init__(self, capacity: int):
        self._data = list()
        self._capacity = capacity

    def __contains__(self, item) -> bool: #operator in
        return item in self._data
    
    def random_item(self) -> any:
        index = randrange(0, len(self._data))
        return self._data[index]

    def get_items(self) -> list:
        return list(self._data)

    def insert(self, item) -> None:
        if len(self._data) < self._capacity:
            self._data.append(item)
        else:
            assert len(self._data) == self._capacity, "error brah"
            index = randrange(0, self._capacity) #nahodny index obeti na prepsani
            self._data[index] = item #prepsani prvku

    def __len__(self) -> int:
        return len(self._data)
    
    def __iter__(self):
        return iter(self._data)
    
    def __repr__(self) -> str:
        return repr(self._data)

def queue_test():
    r = Queue(["l","g","f"])

    r.enqueue("prvek")
    print(r.front())
    print(r.dequeue())
    print(r.rear())
    print(r.isEmpty())
    print(r.size())
    r.enqueue("prvek")
    r.enqueue("prvek")
    r.enqueue("prvek")
    r.enqueue("prvek")
    r.enqueue("prvek")
    r.enqueue("prvek")
    r.enqueue("prvek")
    r.enqueue("prvek")
    r.enqueue("prvek")
    r.enqueue("prvek")
    r.enqueue("prvek")


    l = list()

def stack_test():
    s = Stack()

    s.push("zzz")
    print(s)
    print(len(s))
    s.pop()
    
    s.push("sss")
    print(s.items)

def sklero_test():
    cisla = ScleroticSet(10)

    for i in range(20):
        cisla.insert(i)
    
    print(cisla.get_items())
    [print(item) for item in cisla]

    #print(cisla.random_item())

def syntax(input) -> bool:
    expected = Stack()
    pairs = {
        #"(":")",
        ")":"(",
        #"{":"}",
        "}":"{",
        #"[":"]",
        "]":"["
    }
    
    for i in input:
        if i in pairs:
            if i == expected.peek():
                expected.pop()
            else:
                expected.push(pairs[i])

    return True if expected.isEmpty() else False

#queue_test()
#stack_test()
#sklero_test()
print(syntax("[{(8+5)-(65*8)}+(1*9)]+(56-8)"))
print(syntax(")8-8("))
print(syntax(")8-8(}"))