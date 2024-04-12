import numpy

def counting(seznam):
    
    max = 0

    for _ in range(len(seznam)):
        if seznam[_] > max:
            max = seznam[_]
    
    c = [0] * (max+1)
    for _ in range(len(seznam)):
        c[seznam[_]] = seznam.count(seznam[_])
    
    cs = numpy.cumsum(c)

    ns = [0] * len(seznam)

    for cislo in reversed(seznam):
        cs[cislo] -= 1

        ns[cs[cislo]] = cislo
        

    return ns
def bucket(seznam, k = 10):
    bckts = numpy.linspace(0, 9, k)
    dic = {}

    for _ in range(len(seznam)):
        for a in bckts:
            if round(seznam[_], 1)*10 == a:
                if a in dic.keys():
                    dic[a].append(seznam[_])
                else: 
                    dic[a] = seznam[_]
        



    return dic
def merge_sort(seznam): #TODO
    if len(seznam)  == 1:
        return seznam
    elif len(seznam) == 2:
        if seznam[0] > seznam[1]:
            seznam[0], seznam[1] = seznam[1], seznam[0]
            return seznam
        else:
            return seznam
    elif seznam == sorted(seznam):
        return seznam
    else:
        merge_sort([int(seznam[i]) for i in range(len(seznam)) if i % 2 == 0])
        merge_sort([int(seznam[i]) for i in range(len(seznam)) if i % 2 != 0])


if __name__ == "__main__":
    print(counting([1,3,2,3,0,5, 85, 4, 96, 2 ,0 ,1]))
    #print(bucket([0.12,0.45,0.14,0.91]))
    print(merge_sort([1,3,2,3,0,5, 85, 4, 96, 2 ,0 ,1]))
