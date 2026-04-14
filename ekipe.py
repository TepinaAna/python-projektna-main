from typing import List, Dict

from nba_api.stats.static import teams


def pridobi_seznam_ekip() -> List[Dict[str, str]]:
    """
    Pridobi seznam NBA ekip.
    """
    vse_ekipe = teams.get_teams()

    rezultat = []
    for ekipa in vse_ekipe:
        rezultat.append({
            "id": ekipa["id"],
            "ime": ekipa["full_name"],
            "kratica": ekipa["abbreviation"],
            "mesto": ekipa["city"],
            "vzdevek": ekipa["nickname"],
            "drzava": ekipa["state"],
        })

    return rezultat
