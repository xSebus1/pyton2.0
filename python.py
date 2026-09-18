import math

def farenheit(temperatura: float):
    przelicznik = (temperatura * 1.8) + 32
    return przelicznik

def checkNum(numb: int):
    if numb % 2 == 0:
        return True
    else:
        return False
    
def Hello(name: str):
    zwrot = "Cześć"
    return zwrot ," ", name, "!"

def minMax(liczby):
    if not liczby:
        return None
    return (min(liczby), max(liczby))

def zlicz_samogloski(tekst):
    samogloski = "aeiouyAEIOUY"
    
    return sum(1 for znak in tekst if znak in samogloski)

def filtrujListe(numbers):
    return [num for num in numbers if num > 0]

def oblicznowa(cena, rabat):
    if cena < 0 or not (0 <= rabat <= 100):
        return None
    
    cena_koncowa = cena * (1 - rabat / 100)
    return round(cena_koncowa, 2)

def analiza(tekst):
    return {
        "dlugosc": len(tekst),
        "ilosc_slow": len(tekst.split()),
        "ilosc_spacji": tekst.count(' ')
    }
    
def wieleargumentow(*args):
    if not args:
        return 0
    return sum(args) / len(args)

def pole(promien):
    return math.pi * promien ** 2

def objetosc(promien, wysokosc):
    podstawa = pole(promien)
    return podstawa * wysokosc

def palindron(palindron):
    podstawa = palindron.lower()
    if podstawa[::1] == podstawa:
        return True
    else:
        return False
    
def trycatch(tekst):
    try:
        return int(tekst)
    except ValueError:
        return None

def incijaly(pelne_imie):
    slowa = pelne_imie.split()
    inicjaly = [slowo[0].upper() + '.' for slowo in slowa]
    
    return "".join(inicjaly)

xd = incijaly("Sebastian SAafdafa")
print(xd)
    
    
def nowalista(elementy):
    return list(set(elementy))

def wielearg(username, **kwargs):
    return {"username": username, **kwargs}

def czy_anagram(tekst1, tekst2):
    s1 = "".join(tekst1.lower().split())
    s2 = "".join(tekst2.lower().split())
    
    return sorted(s1) == sorted(s2)

def potworzenia(elementy):
    ile = {}
    for element in elementy:
        ile[element] = ile.get(element, 0) + 1
    return ile

def karta(text):
  if len(text) < 4:
    return text
  return "*" * (len(text) - 4) + text[-4:]

def rozwiaz(a, b):
    if a == 0:
        if b == 0:
            return "tozsamosciowe"
        else:
            return "sprzeczne"
    else:
        return -b / a

def modulo(dzielna, dzielnik):
  if dzielnik == 0:
    return None
  return (dzielna // dzielnik, dzielna % dzielnik)

def lista(lista):
  listaa = []
  for wiersz in lista:
    for element in lista:
        lista.append(element)
  return listaa

def dlugosc(slowa, min_dlugosc):
  wynik = []
  for slowo in slowa:
    if len(slowo) >= min_dlugosc:
      wynik.append(slowo)
  return wynik

def checkOdwroc(zdanie):
    slowa = zdanie.split()
    
    noweslowo = slowa[::-1]
    return " ".join(noweslowo)

def checkAge(wiek):
    if wiek <= 12:
        return "Dziecko"
    elif wiek >= 13 and wiek < 18:
        return "Nastolatek"
    elif wiek >= 18 and wiek < 65:
        return "Dorosły"
    elif wiek >= 65:
        return "Senior"

def czas(sekund):
    godziny = sekund // 3600
    reszta = sekund % 3600
    minuty = reszta // 60
    sekundReszta = reszta % 60

    return f"{godziny}:{minuty}:{sekundReszta}"
