from typing import Optional, Dict, List

from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo


def najdi_igralca(ime_igralca: str) -> Optional[Dict[str, str]]:
    """
    Poišče igralca po polnem imenu.
    """
    kandidati: List[Dict] = players.find_players_by_full_name(ime_igralca)

    if not kandidati:
        return None

    igralec = kandidati[0]

    return {
        "id": igralec["id"],
        "ime": igralec["full_name"],
        "aktivni": igralec["is_active"],
    }


def pridobi_podatke_igralca(player_id: int) -> Dict[str, str]:
    """
    Pridobi osnovne podatke igralca preko nba_api.
    """
    odgovor = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    dfs = odgovor.get_data_frames()

    if not dfs:
        return {"napaka": "Podatkov ni bilo mogoče pridobiti."}

    df = dfs[0]
    if df.empty:
        return {"napaka": "Podatkov ni bilo mogoče pridobiti."}

    vrstica = df.iloc[0]

    return {
        "id": int(vrstica.get("PERSON_ID", 0)),
        "ime": str(vrstica.get("DISPLAY_FIRST_LAST", "")),
        "rojstvo": str(vrstica.get("BIRTHDATE", "")),
        "sola": str(vrstica.get("SCHOOL", "")),
        "drzava": str(vrstica.get("COUNTRY", "")),
        "visina": str(vrstica.get("HEIGHT", "")),
        "teza": str(vrstica.get("WEIGHT", "")),
        "sezona": str(vrstica.get("SEASON_EXP", "")),
        "pozicija": str(vrstica.get("POSITION", "")),
        "ekipa": str(vrstica.get("TEAM_NAME", "")),
        "stevilka": str(vrstica.get("JERSEY", "")),
    }
