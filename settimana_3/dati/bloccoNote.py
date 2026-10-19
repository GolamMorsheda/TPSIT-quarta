def salva_appunto(testo):
    with open("appunti.txt", "a", encoding="utf-8") as f:
        f.write(testo + "\n")

salva_appunto("comprare il libro")
salva_appunto("ripassare i file")
salva_appunto("consegnare su GitHub")

with open("appunti.txt", "r", encoding="utf-8") as f:
    #il numero diventa 1 al primo ciclo. e la riga diventa "comprare il libro"
    #al secondo giro il numero diventa 2 e la riga diventa "ripassare i file"
    for numero, riga in enumerate(f, start=1): #contatore, l'elemento della lista, IN sta per da dove estrare i dati
          print(numero, riga.strip()) #strip toglie il carattere invisibile "\n"