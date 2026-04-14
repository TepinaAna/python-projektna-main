import os
import matplotlib.pyplot as plt
from typing import List, Dict

from analiza import izracunaj_povprecje


def _ustvari_mapo() -> None:
    os.makedirs("izpisi", exist_ok=True)


def stolpicni_diagram(
    ime1: str,
    game_log1: List[Dict[str, str]],
    ime2: str,
    game_log2: List[Dict[str, str]],
    shrani: bool = True,
    prikazi: bool = True,
) -> None:
    """
    Naredi stolpični diagram za primerjavo dveh igralcev.
    Lahko ga shrani kot PNG in/ali prikaže na zaslonu.
    """
    _ustvari_mapo()

    p1 = izracunaj_povprecje(game_log1)
    p2 = izracunaj_povprecje(game_log2)

    kategorije = ["Točke", "Skoki", "Asistence"]
    vrednosti1 = [p1["povp_tocke"], p1["povp_skoki"], p1["povp_asistence"]]
    vrednosti2 = [p2["povp_tocke"], p2["povp_skoki"], p2["povp_asistence"]]

    x = range(len(kategorije))
    width = 0.35

    x1 = [i - width / 2 for i in x]
    x2 = [i + width / 2 for i in x]

    plt.figure()
    plt.bar(x1, vrednosti1, width=width, label=ime1)
    plt.bar(x2, vrednosti2, width=width, label=ime2)

    plt.xticks(list(x), kategorije)
    plt.title(f"{ime1} vs {ime2}")
    plt.xlabel("Kategorije")
    plt.ylabel("Povprečje")
    plt.legend()

    ime_datoteke = f"izpisi/stolpicni_{ime1}_{ime2}.png".replace(" ", "_")

    if shrani:
        plt.savefig(ime_datoteke, dpi=300, bbox_inches="tight")
        print(f"Graf shranjen: {ime_datoteke}")

    if prikazi:
        plt.show()

    plt.close()


def tortni_diagram(
    ime: str,
    game_log: List[Dict[str, str]],
    shrani: bool = True,
    prikazi: bool = True,
) -> None:
    """
    Naredi tortni diagram za igralca.
    Lahko ga shrani kot PNG in/ali prikaže na zaslonu.
    """
    _ustvari_mapo()

    p = izracunaj_povprecje(game_log)

    oznake = ["Točke", "Skoki", "Asistence"]
    vrednosti = [
        p["povp_tocke"],
        p["povp_skoki"],
        p["povp_asistence"],
    ]

    plt.figure()
    plt.pie(vrednosti, labels=oznake, autopct="%1.1f%%")
    plt.title(f"Statistika: {ime}")

    ime_datoteke = f"izpisi/tortni_{ime}.png".replace(" ", "_")

    if shrani:
        plt.savefig(ime_datoteke, dpi=300, bbox_inches="tight")
        print(f"Graf shranjen: {ime_datoteke}")

    if prikazi:
        plt.show()

    plt.close()
