import json
import os
from typing import Any


def _ustvari_mapo_ce_ne_obstaja(pot: str) -> None:
    mapa = os.path.dirname(pot)
    if mapa:
        os.makedirs(mapa, exist_ok=True)


def shrani_json(pot: str, podatki: Any) -> None:
    """
    Shrani podatke v JSON datoteko.
    """
    _ustvari_mapo_ce_ne_obstaja(pot)
    with open(pot, "w", encoding="utf-8") as datoteka:
        json.dump(podatki, datoteka, ensure_ascii=False, indent=4)


def shrani_txt(pot: str, vsebina: str) -> None:
    """
    Shrani besedilo v TXT datoteko.
    """
    _ustvari_mapo_ce_ne_obstaja(pot)
    with open(pot, "w", encoding="utf-8") as datoteka:
        datoteka.write(vsebina)
