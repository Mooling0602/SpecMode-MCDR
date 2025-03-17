import minecraft_data_api as dapi
import spec_mode.data as data

from mcdreforged.api.all import *


def get_player_pos(player: str) -> dict:
    position: list = dapi.get_player_info(player, "Pos")
    dimension: str = dapi.get_player_info(player, "Dimension")
    data = {
        'position': position,
        'dimension': dimension
    }
    return data

def record_player_pos(player: str):
    pos = get_player_pos(player)
    data.positions[player] = pos
