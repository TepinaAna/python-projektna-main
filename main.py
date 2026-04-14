from igralci import najdi_igralca, pridobi_podatke_igralca
from tekme import pridobi_game_log_igralca
from ekipe import pridobi_seznam_ekip
from analiza import primerjaj_igralca
from shrani import shrani_json, shrani_txt
from grafi import stolpicni_diagram, tortni_diagram


def meni() -> None:
    print("\n=== BASKETBALL PROJECT (NBA API) ===")
    print("1. Poišči igralca")
    print("2. Pridobi podatke igralca")
    print("3. Pridobi game log igralca")
    print("4. Primerjaj dva igralca")
    print("5. Seznam ekip")
    print("6. Stolpični diagram (primerjava)")
    print("7. Tortni diagram (igralec)")
    print("0. Izhod")


def main() -> None:
    while True:
        meni()
        izbira = input("Izberi možnost: ").strip()

        try:
            if izbira == "1":
                ime = input("Vnesi ime igralca: ").strip()
                rezultat = najdi_igralca(ime)
                if rezultat:
                    print("\nNajden igralec:")
                    for k, v in rezultat.items():
                        print(f"{k}: {v}")
                else:
                    print("Igralec ni bil najden.")

            elif izbira == "2":
                ime = input("Vnesi ime igralca: ").strip()
                igralec = najdi_igralca(ime)
                if not igralec:
                    print("Igralec ni bil najden.")
                    continue

                podatki = pridobi_podatke_igralca(igralec["id"])
                print("\nPodatki igralca:")
                for k, v in podatki.items():
                    print(f"{k}: {v}")

                shrani = input("Ali želiš shraniti podatke v JSON? (da/ne): ").strip().lower()
                if shrani == "da":
                    shrani_json("podatki/igralci.json", podatki)
                    print("Shranjeno v podatki/igralci.json")

            elif izbira == "3":
                ime = input("Vnesi ime igralca: ").strip()
                sezona = input("Vnesi sezono (npr. 2023-24 ali 2024): ").strip()

                igralec = najdi_igralca(ime)
                if not igralec:
                    print("Igralec ni bil najden.")
                    continue

                game_log = pridobi_game_log_igralca(igralec["id"], sezona)
                if not game_log:
                    print("Game log ni bil najden.")
                    continue

                print(f"\nPrvih 5 tekem za {ime}:")
                for tekma in game_log[:5]:
                    print(tekma)

                shrani = input("Ali želiš shraniti game log v JSON? (da/ne): ").strip().lower()
                if shrani == "da":
                    shrani_json("podatki/tekme.json", game_log)
                    print("Shranjeno v podatki/tekme.json")

            elif izbira == "4":
                ime1 = input("Vnesi ime prvega igralca: ").strip()
                ime2 = input("Vnesi ime drugega igralca: ").strip()
                sezona = input("Vnesi sezono (npr. 2023-24 ali 2024): ").strip()

                igralec1 = najdi_igralca(ime1)
                igralec2 = najdi_igralca(ime2)

                if not igralec1 or not igralec2:
                    print("Eden ali oba igralca nista bila najdena.")
                    continue

                game_log1 = pridobi_game_log_igralca(igralec1["id"], sezona)
                game_log2 = pridobi_game_log_igralca(igralec2["id"], sezona)

                if not game_log1 or not game_log2:
                    print("Za enega od igralcev ni bilo mogoče pridobiti game loga.")
                    continue

                analiza = primerjaj_igralca(ime1, game_log1, ime2, game_log2)
                print("\nPrimerjava igralcev:")
                print(analiza)

                shrani = input("Ali želiš shraniti primerjavo v TXT? (da/ne): ").strip().lower()
                if shrani == "da":
                    shrani_txt("izpisi/primerjava_igralcev.txt", analiza)
                    print("Shranjeno v izpisi/primerjava_igralcev.txt")

            elif izbira == "5":
                ekipe = pridobi_seznam_ekip()
                if not ekipe:
                    print("Ni bilo mogoče pridobiti seznama ekip.")
                    continue

                print("\nSeznam ekip:")
                for ekipa in ekipe:
                    print(f"- {ekipa['ime']} ({ekipa['kratica']})")

            elif izbira == "0":
                print("Izhod iz programa.")
                break
            
            elif izbira == "6":
                ime1 = input("Prvi igralec: ").strip()
                ime2 = input("Drugi igralec: ").strip()
                sezona = input("Sezona (npr. 2024): ").strip()

                igralec1 = najdi_igralca(ime1)
                igralec2 = najdi_igralca(ime2)

                if not igralec1 or not igralec2:
                    print("Igralec ni najden.")
                    continue

                g1 = pridobi_game_log_igralca(igralec1["id"], sezona)
                g2 = pridobi_game_log_igralca(igralec2["id"], sezona)

                stolpicni_diagram(ime1, g1, ime2, g2)
            elif izbira == "7":
                ime = input("Igralec: ").strip()
                sezona = input("Sezona (npr. 2024): ").strip()

                igralec = najdi_igralca(ime)
                if not igralec:
                    print("Igralec ni najden.")
                    continue

                g = pridobi_game_log_igralca(igralec["id"], sezona)

                tortni_diagram(ime, g)
            else:
                print("Neveljavna izbira.")


        except Exception as e:
            print(f"\nNapaka: {e}\n")


if __name__ == "__main__":
    main()
