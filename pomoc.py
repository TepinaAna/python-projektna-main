from typing import Optional


def normaliziraj_sezono(sezona: str) -> str:
    """
    Sprejme:
    - 2024  -> vrne 2023-24
    - 2023-24 -> vrne 2023-24
    """
    sezona = sezona.strip()

    if "-" in sezona:
        return sezona

    if sezona.isdigit() and len(sezona) == 4:
        konec = int(sezona)
        zacetek = konec - 1
        kratko = str(konec)[-2:]
        return f"{zacetek}-{kratko}"

    raise ValueError("Neveljaven zapis sezone. Uporabi npr. 2024 ali 2023-24.")


def varno_int(vrednost: Optional[str], default: int = 0) -> int:
    try:
        return int(vrednost)
    except (TypeError, ValueError):
        return default


def varno_float(vrednost: Optional[str], default: float = 0.0) -> float:
    try:
        return float(vrednost)
    except (TypeError, ValueError):
        return default
