
person = {'Nume': 'Vasile', 'Varsta': 80.3232, 'Pasiuni': ['Bautura', 'Distractie', 'Plimbari']}

def output(info, **kwargs):
    hobby = person["Pasiuni"]
    print(f' {info["Nume"]:15} {info["Varsta"]:= .2f}' + " "*10 + " ".join(hobby))

output(person)


lista_persoane = [{"Nume": "Murel", "Profesie": "Lacatus", "Ani de Scoala": 12, "Vechime": 40, "Salariu": 2600},
{"Nume": "Viorel", "Profesie": "Tehnician IT", "Ani de Scoala": 8, "Vechime": 8, "Salariu": 10000},
{"Nume": "Borcea", "Profesie": "Inginer Retea", "Ani de Scoala": 12, "Vechime": 8, "Salariu": 4000}
]

def creare_tabel(lista_persoane, **kwargs):
    for persoana in lista_persoane:
        print("{Nume:>15} {Profesie:>15} {Ani de Scoala:*=15} {Vechime:*^15} {Salariu:^15}".format(**persoana))

creare_tabel(lista_persoane)