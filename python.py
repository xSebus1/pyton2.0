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
    
