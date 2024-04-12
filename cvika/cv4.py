def bubble(seznam):
    for a in range(len(seznam)):
        serazeno = True
        for i in range(len(seznam)-1-a):
            if seznam[i] > seznam[i+1]:
                seznam[i], seznam[i+1] = seznam[i+1], seznam[i]
                serazeno = False
        if serazeno:
            return seznam
        
def selection(seznam):
    
    result = list()

    while True:

        nejmensi_index = 0

        for i in range(len(seznam)):
            if seznam[i] <= seznam[nejmensi_index]:
                
                nejmensi_index = i

        if not seznam:
            return result
        else:
            result.append(seznam.pop(nejmensi_index))


def fibo(n):
    assert n > -1

    return n if n < 2 else fibo(n-2) + fibo(n-1)



def quick(seznam):
    if len(seznam) < 2: return seznam
    pivot = seznam.pop()
    return quick([prvek for prvek in seznam if prvek <= pivot]) + [pivot] + quick([prvek for prvek in seznam if prvek > pivot])
    


    
print(fibo(11))


seznam = [8,5,4,7,6,9,8,1,1,2,4,3,5,7,8,94,1,22,64,1,0,67,125,157,9,77,6,94,-45,-78,-1,-65741,-997,-5511,6e52,-85e69]
print(quick(seznam))
print(quick([90,11,38,50,1,97]))


# seznam = [8,5,4,7,6,9,8,1,1,2,4,3,5,7,8,94,1,22,64,1,0,67,125,157,9,77,6,94,-45,-78,-1,-65741,-997,-5511,6e52,-85e69]
# print(bubble(seznam))
# seznam = [8,5,4,7,6,9,8,1,1,2,4,3,5,7,8,94,1,22,64,1,0,67,125,157,9,77,6,94,-45,-78,-1,-65741,-997,-5511,6e52,-85e69]
# print(selection(seznam))