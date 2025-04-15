import json

# filepath: cennik.json
# Wczytanie cennika z pliku
def wczytaj_cennik(plik):
    with open(plik, 'r', encoding='utf-8') as f:
        return json.load(f)

# Wyświetlenie dostępnych biletów
def wyswietl_cennik(cennik):
    print("\nDostępne bilety:")
    for typ, kategorie in cennik.items():
        print(f"\n{typ.capitalize()}:")
        for kategoria, bilety in kategorie.items():
            print(f"  {kategoria.capitalize()}:")
            for nazwa, cena in bilety.items():
                print(f"    {nazwa}: {cena} zł")

# Dodanie biletu do koszyka
def dodaj_do_koszyka(cennik, koszyk):
    while True:
        typ = input("\nWybierz typ biletu (n - normalny, u - ulgowy): ").lower()
        if typ in ['n', 'u']:
            typ = 'normalny' if typ == 'n' else 'ulgowy'
            break
        print("Nieprawidłowy wybór. Spróbuj ponownie.")

    kategorie = list(cennik[typ].keys())
    for i, kategoria in enumerate(kategorie):
        print(f"{i + 1}. {kategoria.capitalize()}")
    while True:
        wybor_kategorii = input("Wybierz kategorię biletu (cyfra): ")
        if wybor_kategorii.isdigit() and 1 <= int(wybor_kategorii) <= len(kategorie):
            kategoria = kategorie[int(wybor_kategorii) - 1]
            break
        print("Nieprawidłowy wybór. Spróbuj ponownie.")

    bilety = list(cennik[typ][kategoria].keys())
    for i, bilet in enumerate(bilety):
        print(f"{i + 1}. {bilet} - {cennik[typ][kategoria][bilet]} zł")
    while True:
        wybor_biletu = input("Wybierz bilet (cyfra): ")
        if wybor_biletu.isdigit() and 1 <= int(wybor_biletu) <= len(bilety):
            bilet = bilety[int(wybor_biletu) - 1]
            break
        print("Nieprawidłowy wybór. Spróbuj ponownie.")

    koszyk.append((typ, kategoria, bilet, cennik[typ][kategoria][bilet]))
    print(f"\nDodano do koszyka: {bilet} - {cennik[typ][kategoria][bilet]} zł")

# Obliczenie reszty
def oblicz_reszte(do_zaplaty, zaplacono):
    return round(zaplacono - do_zaplaty, 2)

# Finalizacja transakcji
def dokonaj_platnosci(koszyk):
    suma = sum(bilet[3] for bilet in koszyk)
    print(f"\nDo zapłaty: {suma} zł")
    while True:
        try:
            zaplacono = float(input("Podaj kwotę, którą płacisz: "))
            if zaplacono >= suma:
                reszta = oblicz_reszte(suma, zaplacono)
                print(f"Transakcja zakończona. Twoja reszta: {reszta} zł")
                break
            else:
                print("Podana kwota jest za mała. Spróbuj ponownie.")
        except ValueError:
            print("Nieprawidłowa kwota. Spróbuj ponownie.")

# Główna funkcja programu
def automat_biletowy():
    cennik = wczytaj_cennik('prices.json')
    koszyk = []

    while True:
        print("\n1. Wyświetl cennik")
        print("2. Dodaj bilet do koszyka")
        print("3. Pokaż koszyk")
        print("4. Dokonaj płatności")
        print("5. Wyjdź")
        wybor = input("Wybierz opcję (cyfra): ")

        if wybor == '1':
            wyswietl_cennik(cennik)
        elif wybor == '2':
            dodaj_do_koszyka(cennik, koszyk)
        elif wybor == '3':
            print("\nKoszyk:")
            for bilet in koszyk:
                print(f"{bilet[2]} - {bilet[3]} zł")
        elif wybor == '4':
            dokonaj_platnosci(koszyk)
            koszyk.clear()
        elif wybor == '5':
            print("Dziękujemy za skorzystanie z automatu biletowego!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    automat_biletowy()