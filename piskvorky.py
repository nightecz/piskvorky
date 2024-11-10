def vykresli_pole(pole):
    for radek in pole:
        print(' | '.join(radek))
        print('-' * (len(radek) * 4 - 1))


def vyhodnot(pole):
    # Kontrola řádků
    for radek in pole:
        if all(policko == 'X' for policko in radek):
            return 'X'
        elif all(policko == 'O' for policko in radek):
            return 'O'

    # Kontrola sloupců
    for i in range(len(pole)):
        if all(pole[j][i] == 'X' for j in range(len(pole))):
            return 'X'
        elif all(pole[j][i] == 'O' for j in range(len(pole))):
            return 'O'

    # Kontrola diagonál
    if all(pole[i][i] == 'X' for i in range(len(pole))) or all(
            pole[i][len(pole) - 1 - i] == 'X' for i in range(len(pole))):
        return 'X'
    elif all(pole[i][i] == 'O' for i in range(len(pole))) or all(
            pole[i][len(pole) - 1 - i] == 'O' for i in range(len(pole))):
        return 'O'

    # Kontrola remízy
    if all(all(policko != '-' for policko in radek) for radek in pole):
        return 'remiza'

    # Pokračuje hra
    return None


def tah_hrace(pole, symbol):
    while True:
        try:
            souradnice = input("Zadejte souřadnice ve formátu 'radek,sloupec': ").split(',')
            radek = int(souradnice[0]) - 1
            sloupec = int(souradnice[1]) - 1
            if pole[radek][sloupec] == '-':
                pole[radek][sloupec] = symbol
                break
            else:
                print("Toto pole je již obsazeno, zvolte jiné.")
        except (ValueError, IndexError):
            print("Neplatný vstup. Zadejte prosím souřadnice ve formátu 'radek,sloupec'.")


def tah_pocitace(pole, symbol):
    from random import randint
    while True:
        radek = randint(0, len(pole) - 1)
        sloupec = randint(0, len(pole) - 1)
        if pole[radek][sloupec] == '-':
            pole[radek][sloupec] = symbol
            break


def hra_piskvorek():
    velikost_pole = 3
    pole = [['-' for _ in range(velikost_pole)] for _ in range(velikost_pole)]
    symbol_hrace = 'X'
    symbol_pocitace = 'O'

    while True:
        vykresli_pole(pole)
        if symbol_hrace == 'X':
            tah_hrace(pole, symbol_hrace)
        else:
            tah_pocitace(pole, symbol_hrace)

        vitez = vyhodnot(pole)
        if vitez:
            vykresli_pole(pole)
            if vitez == 'remiza':
                print("Remíza!")
            else:
                print(f"Vítěz je {vitez}!")
            break

        symbol_hrace, symbol_pocitace = symbol_pocitace, symbol_hrace


hra_piskvorek()