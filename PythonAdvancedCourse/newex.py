import math

list1 = [(4, 'e'), (3, 'a'), (2, 'x')]
list2 = ['mere', 'pere', 'prune', 'gutui', 'sare']

mapping = list(map(lambda elem, elem1: (elem[0], elem1), list1, list2))
# print(mapping)

list1.sort(key=lambda x: x[0])
# print(list1)

def filt(l):
    for item in l:
        for letter in item:
            if letter == 'e':
                return item


filtred_list = list(filter(filt, list2))
print(filtred_list)

filtred_list1 = lambda list: True if list[0].startswith('m') else False

print(filtred_list1(list2[0]))

n = 432
s = 0
while n != 0:
    n = n // 10
    s = s + 1

# print(s)

n = 123456
inv = 0

while n != 0:
    c = n % 10
    inv = (inv * 10) + c
    n = n // 10

# print(inv)

def number():
    list1 = []
    for n in range(1, 100):
        list1.append(n)
    return list1




def functie_nr_prim(numar):
    if numar > 1:
        for i in range(2, numar):
            if (numar % i) == 0:
                break
        else:
            return True

functie_nr_prim(25)

lista_prm = []

for i in number():
    if functie_nr_prim(i) is True:
        lista_prm.append(i)


print(lista_prm)





