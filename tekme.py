from typing import List, Dict

from nba_api.stats.endpoints import playergamelog

from pomoc import normaliziraj_sezono


def pridobi_game_log_igralca(player_id: int, sezona: str) -> List[Dict[str, str]]:
    """
    Pridobi game log igralca za izbrano sezono.
    """
    sezona_api = normaliziraj_sezono(sezona)

    odgovor = playergamelog.PlayerGameLog(player_id=player_id, season=sezona_api)
    dfs = odgovor.get_data_frames()

    if not dfs:
        return []

    df = dfs[0]
    if df.empty:
        return []

    rezultat = []

    for _, vrstica in df.iterrows():
        tekma = {
            "game_id": str(vrstica.get("Game_ID", "")),
            "datum": str(vrstica.get("GAME_DATE", "")),
            "nasprotnik": str(vrstica.get("MATCHUP", "")),
            "rezultat": str(vrstica.get("WL", "")),
            "min": str(vrstica.get("MIN", "")),
            "tocke": str(vrstica.get("PTS", "")),
            "skoki": str(vrstica.get("REB", "")),
            "asistence": str(vrstica.get("AST", "")),
            "ukradene": str(vrstica.get("STL", "")),
            "blokade": str(vrstica.get("BLK", "")),
            "izgubljene": str(vrstica.get("TOV", "")),
            "met_iz_igre": str(vrstica.get("FGM", "")),
            "poskusi_iz_igre": str(vrstica.get("FGA", "")),
            "trojke": str(vrstica.get("FG3M", "")),
            "poskusi_trojk": str(vrstica.get("FG3A", "")),
            "prosti_met": str(vrstica.get("FTM", "")),
            "poskusi_prostih_metov": str(vrstica.get("FTA", "")),
            "plus_minus": str(vrstica.get("PLUS_MINUS", "")),
        }
        rezultat.append(tekma)

    return rezultat
