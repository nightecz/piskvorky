def vykresli_pole(pole):
    """
    Vykreslí herní pole.

    Args:
        pole (list of list of str): Herní pole jako seznam seznamů řádků.
    """
    for radek in pole:
        print(' | '.join(radek))
        print('-' * (len(radek) * 4 - 1))


def vyhodnot(pole):
    """
    Vyhodnotí stav hry.

    Args:
        pole (list of list of str): Herní pole jako seznam seznamů řádků.

    Returns:
        str: 'X' pokud vyhrál hráč s 'X', '0' pokud vyhrál hráč s 'O', 'remíza' pokud je remíza, None pokud hra pokračuje .
    """
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
    """
    Zpracuje tah hráče.

    Args:
        pole (list of list of str): Herní pole jako seznam seznamů řádků.
        symbol (str): Symmbol hráče ('X' nebo 'O').
    """
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
    """
    Zpracuje tah počítače.

    Args:
        pole (list of list of str): Herní pole jako seznam seznamů řádků.
        symbol (str): Symbol počítače ('X' nebo '0').
    """
    from random import randint
    while True:
        radek = randint(0, len(pole) - 1)
        sloupec = randint(0, len(pole) - 1)
        if pole[radek][sloupec] == '-':
            pole[radek][sloupec] = symbol
            break


def hra_piskvorek():
    """
    Spustí hru piškvorky.
    """
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
