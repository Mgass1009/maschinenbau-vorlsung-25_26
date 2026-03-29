# eingabe = input("eingabe Zahl: ")

# zahl = int(eingabe)

try:
    zahl = int(input("Gib eine Zahl ein: "))
    ergebnis = 100 / zahl
    print(f"Ergebnis: {ergebnis}")
except ValueError as e:
    print("Fehler: Keine gültige Zahl eingegeben!")
except ZeroDivisionError as e:
    print("Fehler: Division durch Null ist nicht erlaubt!")
finally:
    print("wird immer ausgegeben")