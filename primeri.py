from igralci import najdi_igralca, pridobi_podatke_igralca
from tekme import pridobi_game_log_igralca
from ekipe import pridobi_seznam_ekip
from analiza import primerjaj_igralca
from grafi import stolpicni_diagram, tortni_diagram
from shrani import shrani_json, shrani_txt


def primer_1_poisci_igralca() -> None:
    print("\n" + "=" * 60)
    print("PRIMER 1: POIŠČI IGRALCA")
    print("=" * 60)

    ime = "Luka Doncic"
    rezultat = najdi_igralca(ime)

    if rezultat:
        print(f"Iščem igralca: {ime}")
        print("Najden igralec:")
        for k, v in rezultat.items():
            print(f"{k}: {v}")
    else:
        print(f"Igralec {ime} ni bil najden.")


def primer_2_podatki_igralca() -> None:
    print("\n" + "=" * 60)
    print("PRIMER 2: PRIDOBI PODATKE IGRALCA")
    print("=" * 60)

    ime = "Luka Doncic"
    igralec = najdi_igralca(ime)

    if not igralec:
        print(f"Igralec {ime} ni bil najden.")
        return

    podatki = pridobi_podatke_igralca(igralec["id"])

    print(f"Osnovni podatki za: {ime}")
    for k, v in podatki.items():
        print(f"{k}: {v}")

    shrani_json("podatki/primer2_igralec.json", podatki)
    print("Shranjeno v: podatki/primer2_igralec.json")


def primer_3_game_log() -> None:
    print("\n" + "=" * 60)
    print("PRIMER 3: PRIDOBI GAME LOG IGRALCA")
    print("=" * 60)

    ime = "Luka Doncic"
    sezona = "2024"
    igralec = najdi_igralca(ime)

    if not igralec:
        print(f"Igralec {ime} ni bil najden.")
        return

    game_log = pridobi_game_log_igralca(igralec["id"], sezona)

    if not game_log:
        print("Game log ni bil najden.")
        return

    print(f"Prvih 5 tekem za {ime}, sezona {sezona}:")
    for tekma in game_log[:5]:
        print(tekma)

    shrani_json("podatki/primer3_game_log.json", game_log)
    print("Shranjeno v: podatki/primer3_game_log.json")


def primer_4_primerjava_igralcev() -> None:
    print("\n" + "=" * 60)
    print("PRIMER 4: PRIMERJAVA DVEH IGRALCEV")
    print("=" * 60)

    ime1 = "Luka Doncic"
    ime2 = "Stephen Curry"
    sezona = "2024"

    igralec1 = najdi_igralca(ime1)
    igralec2 = najdi_igralca(ime2)

    if not igralec1 or not igralec2:
        print("Eden ali oba igralca nista bila najdena.")
        return

    game_log1 = pridobi_game_log_igralca(igralec1["id"], sezona)
    game_log2 = pridobi_game_log_igralca(igralec2["id"], sezona)

    if not game_log1 or not game_log2:
        print("Za enega od igralcev ni bilo mogoče pridobiti game loga.")
        return

    analiza = primerjaj_igralca(ime1, game_log1, ime2, game_log2)

    print(analiza)

    shrani_txt("izpisi/primer4_primerjava.txt", analiza)
    print("Shranjeno v: izpisi/primer4_primerjava.txt")


def primer_5_seznam_ekip() -> None:
    print("\n" + "=" * 60)
    print("PRIMER 5: SEZNAM EKIP")
    print("=" * 60)

    ekipe = pridobi_seznam_ekip()

    if not ekipe:
        print("Ni bilo mogoče pridobiti seznama ekip.")
        return

    print("Prvih 10 ekip:")
    for ekipa in ekipe[:10]:
        print(f"- {ekipa['ime']} ({ekipa['kratica']})")

    shrani_json("podatki/primer5_ekipe.json", ekipe)
    print("Shranjeno v: podatki/primer5_ekipe.json")


def primer_6_stolpicni_diagram() -> None:
    print("\n" + "=" * 60)
    print("PRIMER 6: STOLPIČNI DIAGRAM")
    print("=" * 60)

    ime1 = "Luka Doncic"
    ime2 = "Stephen Curry"
    sezona = "2024"

    igralec1 = najdi_igralca(ime1)
    igralec2 = najdi_igralca(ime2)

    if not igralec1 or not igralec2:
        print("Eden ali oba igralca nista bila najdena.")
        return

    game_log1 = pridobi_game_log_igralca(igralec1["id"], sezona)
    game_log2 = pridobi_game_log_igralca(igralec2["id"], sezona)

    if not game_log1 or not game_log2:
        print("Ni bilo mogoče pridobiti podatkov za graf.")
        return

    print(f"Odpiram stolpični diagram za {ime1} in {ime2}.")
    stolpicni_diagram(ime1, game_log1, ime2, game_log2)


def primer_7_tortni_diagram() -> None:
    print("\n" + "=" * 60)
    print("PRIMER 7: TORTNI DIAGRAM")
    print("=" * 60)

    ime = "Luka Doncic"
    sezona = "2024"

    igralec = najdi_igralca(ime)

    if not igralec:
        print(f"Igralec {ime} ni bil najden.")
        return

    game_log = pridobi_game_log_igralca(igralec["id"], sezona)

    if not game_log:
        print("Ni bilo mogoče pridobiti podatkov za graf.")
        return

    print(f"Odpiram tortni diagram za {ime}.")
    tortni_diagram(ime, game_log)


def main() -> None:
    print("ZAGON VSEH PRIMEROV 1-7")

    try:
        primer_1_poisci_igralca()
    except Exception as e:
        print(f"Napaka pri primeru 1: {e}")

    try:
        primer_2_podatki_igralca()
    except Exception as e:
        print(f"Napaka pri primeru 2: {e}")

    try:
        primer_3_game_log()
    except Exception as e:
        print(f"Napaka pri primeru 3: {e}")

    try:
        primer_4_primerjava_igralcev()
    except Exception as e:
        print(f"Napaka pri primeru 4: {e}")

    try:
        primer_5_seznam_ekip()
    except Exception as e:
        print(f"Napaka pri primeru 5: {e}")

    try:
        primer_6_stolpicni_diagram()
    except Exception as e:
        print(f"Napaka pri primeru 6: {e}")

    try:
        primer_7_tortni_diagram()
    except Exception as e:
        print(f"Napaka pri primeru 7: {e}")

    print("\nKONEC VSEH PRIMEROV.")


if __name__ == "__main__":
    main()
