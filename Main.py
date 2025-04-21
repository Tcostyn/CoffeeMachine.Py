meniu = {
    "espresso": {
        "ingrediente": {
            "apa": 50,
            "lapte": 0,
            "cafea": 18
        },
        "cost": 15
    },
    "latte": {
        "ingrediente": {
            "apa": 200,
            "lapte": 150,
            "cafea": 24
        },
        "cost": 25
    },
    "cappuccino": {
        "ingrediente": {
            "apa": 250,
            "lapte": 100,
            "cafea": 24
        },
        "cost": 30
    }
}

resurse = {
    "apa": 300,
    "lapte": 200,
    "cafea": 100
}

bani = 0

alegere = input("Ce doriti?(espresso, latte, cappuccino, off, report): ")
if alegere == "off":
    quit()
if alegere == "report":
    print(f"apa: {resurse['apa']}ml")
    print(f"lapte: {resurse['lapte']}ml")
    print(f"cafea: {resurse['cafea']}g")
    print(f"bani: {bani} lei")


def are_resurse(dictionar):
    if dictionar["apa"] > resurse["apa"]:
        print("Scuze! Nu este suficientă apă.")
        return False
    elif dictionar["lapte"] > resurse["lapte"]:
        print("Scuze! Nu este suficient lapte.")
        return False
    elif dictionar["cafea"] > resurse["cafea"]:
        print("Scuze! Nu este suficientă cafea.")
        return False
    return True


def procesare_plata(pret):
    print(f"Ai de achitat {pret} lei. Achita cu monede de 50bani sau bancnote de 1, 5, 10, 20 lei.")
    b_alesi = input("Introduceti cu ce platiti? monede/bancnote: ")
    valoare = int(input("Introduceti cu valoare de bani (a monedei sau bancnotei): "))
    cate = int(input("Cate ai introdus?: "))
    total = valoare * cate

    if total < pret:
        print("Fonduri insuficiente.")
        ok = input("Doriti sa mai introduceti bancnote? da/nu: ")
        if ok == "da":
            valoare1 = int(input("Introduceti cu valoare de bani (a monedei sau bancnotei): "))
            cate1 = int(input("Cate ai introdus?: "))
            total += valoare1 * cate1
        else:
            print("Banii au fost returnați.")
            return False
    print(f"Savureaza cafeaua ta! Rest = {total - pret} lei.")
    return True


def modificare_resurse(alegere):
    global bani
    if alegere == "espresso":
        resurse["apa"] -= meniu["espresso"]["ingrediente"]["apa"]
        resurse["lapte"] -= meniu["espresso"]["ingrediente"]["lapte"]
        resurse["cafea"] -= meniu["espresso"]["ingrediente"]["cafea"]
        bani += meniu["espresso"]["cost"]
    elif alegere == "latte":
        resurse["apa"] -= meniu["latte"]["ingrediente"]["apa"]
        resurse["lapte"] -= meniu["latte"]["ingrediente"]["lapte"]
        resurse["cafea"] -= meniu["latte"]["ingrediente"]["cafea"]
        bani += meniu["latte"]["cost"]
    elif alegere == "cappuccino":
        resurse["apa"] -= meniu["cappuccino"]["ingrediente"]["apa"]
        resurse["lapte"] -= meniu["cappuccino"]["ingrediente"]["lapte"]
        resurse["cafea"] -= meniu["cappuccino"]["ingrediente"]["cafea"]
        bani += meniu["cappuccino"]["cost"]


def ce_folosim(alegere):
    if alegere == "espresso":
        if are_resurse(meniu["espresso"]["ingrediente"]):
            if procesare_plata(meniu["espresso"]["cost"]):
                modificare_resurse(alegere)
    elif alegere == "latte":
        if are_resurse(meniu["latte"]["ingrediente"]):
            if procesare_plata(meniu["latte"]["cost"]):
                modificare_resurse(alegere)
    elif alegere == "cappuccino":
        if are_resurse(meniu["cappuccino"]["ingrediente"]):
            if procesare_plata(meniu["cappuccino"]["cost"]):
                modificare_resurse(alegere)

ce_folosim(alegere)
print(f"Bani în aparat: {bani} lei")
print("Resurse rămase:", resurse)