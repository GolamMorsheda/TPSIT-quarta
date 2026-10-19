def conta_righe(nome_file):
    tot_righe = 0
    piene = 0

    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            tot_righe += 1
            if riga.strip() != "":
                piene += 1

    return tot_righe, piene

for nome in ["settimana_3/dati/parole.txt", "settimana_3/dati/commedia.txt"]:
     tot, piene = conta_righe(nome)
     print(f"{nome}: {tot} righe, {piene} non vuote")