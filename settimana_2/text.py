#liste - qualsiasi tipo
voti = [6, 8, 5, 8, 7]

voti.append(9)
voti.insert(0, 4)
print(voti)

print(voti[0], voti[-1])
print(voti[1:4])

voti.sort()
print(voti)

print(len(voti), 8 in voti)

#set - toglie doppioni
presenze = ["Luca", "Sara", "Marco", "Luca", "Sara"]
unici = set(presenze)

print(len(presenze), "voci registrate")
print(len(unici), "persone diverse")
print(sorted(unici))

#tuple - liste non modificabili
week = ("lun", "mar", "mer", "gio", "ven")
print(week)
print(week[0], week[-1])
print(len(week))

try:
    week[0] = "dom"
except TypeError as errore:
    print("TypeError:", errore)

#dizionari - cerchi per nome
capitali = {"Italia": "Roma", "Francia": "Parigi", "Spagna": "Madrid"}

print(capitali["Italia"])
print(len(capitali))

capitali["Germania"] = "Berlino"
del capitali["Spagna"]
print(capitali)

for paese, citta in capitali.items():
    print(paese, "->", citta)

print(list(capitali.keys()))
print(list(capitali.values()))


#ES1
def conta_unici(nomi):
    return len(set(nomi))

nomi = ["Luca", "Sara", "Marco", "Luca", "Giulia", "Sara", "Luca"]
unici = conta_unici(nomi)
print(unici)

#ES2
def capitale(paese):
    utente = input("inserisci un paese: ")
    if utente in paese:
        return paese[utente]
    else:
        return "paese non in elenco"
    
paese = {"Italia": "Roma", "Francia": "Parigi", "Spagna": "Madrid"}
prova = capitale(paese)
print(prova)

#ES3
def sufficienze(voti):
    nuovi_voti = []
    for voto in voti:
        if voto >= 6:
            nuovi_voti.append(voto)
    return nuovi_voti

voti = [4, 7, 5, 8, 6, 3]
suff = sufficienze(voti)
print(suff)

#ES4
def senza_duplicati(elementi):
    return sorted(set(elementi))

elementi = ["Sara", "Luca", "Sara", "Marco", "Luca", "Giulia"]
unic = senza_duplicati(elementi)
print(unic)