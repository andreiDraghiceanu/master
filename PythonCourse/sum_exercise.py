
def suma(*args):
    suma = 0
    for elem in args:
        suma = suma + elem
    print(suma)

suma(2, 4, 8, 222)

def diferenta(*args):
    diferenta = 0
    for elem in args:
        diferenta = elem - diferenta
    print(diferenta)

diferenta(2, 22, 222)

def produs(*args):
    produs = 1
    for elem in args:
        produs = produs * elem
    print(produs)

produs(2, 4, 5)

def cat(*args):
    cat = 1
    for elem in args:
        cat = elem / cat
    print(cat)

cat(2, 4, 8, 40)

def radacina(*args):
    radacina = 1
    for elem in args:
        radacina = elem  ** 0.5
    print(radacina)

radacina(1000)