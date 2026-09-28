#ES1
def celsius_a_fahrenheit(gradi):
    F = gradi * 9/5 + 32
    return F
gradi = 25
print(f'{gradi}°C corrispondono a {celsius_a_fahrenheit(gradi)}°F')

#ES2
def e_pari(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = 20
i= 1
while i <= num:
    if e_pari(i):
        print(i)
    i += 1

#ES3
def media(voti):
    M = 0
    for voto in voti:
        M += voto
    M = M/len(voti)
    return M

voti = [3, 5, 6]
print(f'La media dei voti è: {media(voti)}')

#ES4
def pullman_necessari(n):
    