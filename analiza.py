from typing import List, Dict

from pomoc import varno_float


def izracunaj_povprecje(game_log: List[Dict[str, str]]) -> Dict[str, float]:
    """
    Izračuna osnovna povprečja igralca iz game loga.
    """
    if not game_log:
        return {
            "tekme": 0,
            "povp_tocke": 0.0,
            "povp_skoki": 0.0,
            "povp_asistence": 0.0,
            "povp_ukradene": 0.0,
            "povp_blokade": 0.0,
        }

    st_tekem = len(game_log)

    vsota_tock = sum(varno_float(t["tocke"]) for t in game_log)
    vsota_skok = sum(varno_float(t["skoki"]) for t in game_log)
    vsota_ast = sum(varno_float(t["asistence"]) for t in game_log)
    vsota_stl = sum(varno_float(t["ukradene"]) for t in game_log)
    vsota_blk = sum(varno_float(t["blokade"]) for t in game_log)

    return {
        "tekme": st_tekem,
        "povp_tocke": round(vsota_tock / st_tekem, 2),
        "povp_skoki": round(vsota_skok / st_tekem, 2),
        "povp_asistence": round(vsota_ast / st_tekem, 2),
        "povp_ukradene": round(vsota_stl / st_tekem, 2),
        "povp_blokade": round(vsota_blk / st_tekem, 2),
    }

def max_min_statistika(game_log):
    if not game_log:
        return {}

    max_tocke = max(float(t["tocke"]) for t in game_log)
    min_tocke = min(float(t["tocke"]) for t in game_log)

    return {
        "max_tocke": max_tocke,
        "min_tocke": min_tocke,
    }

def primerjaj_igralca(
    ime1: str,
    game_log1: List[Dict[str, str]],
    ime2: str,
    game_log2: List[Dict[str, str]],
) -> str:
    """
    Vrne tekstovno primerjavo dveh igralcev.
    """
    p1 = izracunaj_povprecje(game_log1)
    p2 = izracunaj_povprecje(game_log2)

    vrstice = []
    vrstice.append(f"Primerjava igralcev: {ime1} in {ime2}")
    vrstice.append("-" * 50)
    vrstice.append(f"{ime1}:")
    vrstice.append(f"  Tekme: {p1['tekme']}")
    vrstice.append(f"  Točke: {p1['povp_tocke']}")
    vrstice.append(f"  Skoki: {p1['povp_skoki']}")
    vrstice.append(f"  Asistence: {p1['povp_asistence']}")
    vrstice.append(f"  Ukradene žoge: {p1['povp_ukradene']}")
    vrstice.append(f"  Blokade: {p1['povp_blokade']}")
    vrstice.append("")
    vrstice.append(f"{ime2}:")
    vrstice.append(f"  Tekme: {p2['tekme']}")
    vrstice.append(f"  Točke: {p2['povp_tocke']}")
    vrstice.append(f"  Skoki: {p2['povp_skoki']}")
    vrstice.append(f"  Asistence: {p2['povp_asistence']}")
    vrstice.append(f"  Ukradene žoge: {p2['povp_ukradene']}")
    vrstice.append(f"  Blokade: {p2['povp_blokade']}")
    vrstice.append("")
    vrstice.append("Boljši po kategorijah:")

    kategorije = [
        ("Točke", "povp_tocke"),
        ("Skoki", "povp_skoki"),
        ("Asistence", "povp_asistence"),
        ("Ukradene", "povp_ukradene"),
        ("Blokade", "povp_blokade"),
    ]

    for naziv, kljuc in kategorije:
        if p1[kljuc] > p2[kljuc]:
            boljsi = ime1
        elif p2[kljuc] > p1[kljuc]:
            boljsi = ime2
        else:
            boljsi = "Izenačeno"

        vrstice.append(f"  {naziv}: {boljsi}")

    return "\n".join(vrstice)
