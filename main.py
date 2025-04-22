"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Bartlomiej Stefan Krason
email: bart.s.krason@gmail.com
"""

# Registrovaní uživatelé
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Texty k analýze
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Přihlášení
jmeno = input("username: ")
heslo = input("password: ")

# Kontrola přihlášení
if jmeno not in uzivatele:
    print("unregistered user, terminating the program..")
    exit()
elif uzivatele[jmeno] != heslo:
    print("neplatné heslo, terminating the program..")
    exit()

# Přihlášení úspěšné
print("-" * 40)
print(f"Welcome to the app, {jmeno}")
print(f"We have {len(TEXTS)} texts to be analyzed.")
print("-" * 40)

# Výběr textu
vyber = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
print("-" * 40)

# Ověření vstupu
if not vyber.isdigit() or not (1 <= int(vyber) <= len(TEXTS)):
    print("Invalid input. Terminating the program.")
    exit()

# Zpracování textu
text = TEXTS[int(vyber) - 1]
slova = [slovo.strip(".,!?") for slovo in text.split()]

# Statistika
pocet_slov = len(slova)
titlecase = sum(1 for s in slova if s.istitle())
uppercase = sum(1 for s in slova if s.isupper() and s.isalpha())
lowercase = sum(1 for s in slova if s.islower())
cisla = [int(s) for s in slova if s.isdigit()]
soucet = sum(cisla)

# Výstup
print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {len(cisla)} numeric strings.")
print(f"The sum of all the numbers {soucet}")
print("-" * 40)

# Statistiky podle délky slov
delky = {}

for slovo in slova:
    delka = len(slovo)
    delky[delka] = delky.get(delka, 0) + 1

# Výpis tabulky
print("LEN|  OCCURENCES  |NR.")
print("-" * 40)
for delka in sorted(delky):
    hvezdy = '*' * delky[delka]
    print(f"{delka:>3}|{hvezdy:<15}|{delky[delka]}")