import spec_mode.data as data

from mcdreforged.api.all import *
from online_player_api import check_online # type: ignore
from spec_mode.core import record_player_pos


builder = SimpleCommandBuilder()
psi = ServerInterface.psi()

def on_load(server: PluginServerInterface, prev_module):
    for plugin in server.get_plugin_list():
        if plugin == "gamemode":
            server.logger.warning("Conflict plugin found, unloading it!")
            server.unload_plugin("gamemode")
    builder.arg('player', Text)
    builder.register(server)
    server.logger.info("旁观模式插件加载完成！")

@builder.command('!!spec <player>')
@new_thread('SpecMode: MainCommand')
def on_cmd_spec_with_arg(src: CommandSource, ctx: CommandContext):
    if not src.is_console:
        src.reply("玩家参数只能在控制台使用！")
        return
    player = ctx['player']
    if check_online(player) is False:
        src.reply("该玩家不在线或识别异常，无法操作！")
        return
    if data.positions.get(player, None) is None:
        record_player_pos(player)
        psi.execute(f'gamemode spectator {player}')
        src.reply("已使该玩家切换为旁观模式，再次执行此命令以使其退出并返回原位。")
    else:
        pos = data.positions[player].get("position")
        x = str(pos[0])
        y = str(pos[1])
        z = str(pos[2])
        dim = data.positions[player].get("dimension")
        psi.execute(f'execute in {dim} run tp {player} {x} {y} {z}')
        psi.execute(f'gamemode survival {player}')
        src.reply("已使该玩家退出旁观模式并返回原位，再次执行此命令以使其重新开启旁观模式。")
        del data.positions[player]

@builder.command('!!spec')
@new_thread('SpecMode: MainCommand')
def on_cmd_spec(src: CommandSource, ctx: CommandContext):
    if not src.is_player:
        src.reply("控制台执行此命令需提供玩家参数！")
        return
    player = src.player
    if data.positions.get(player, None) is None:
        record_player_pos(player)
        psi.execute(f'gamemode spectator {player}')
        src.reply("已切换为旁观模式，再次执行此命令以退出并返回原位。")
    else:
        pos = data.positions[player].get("position")
        x = str(pos[0])
        y = str(pos[1])
        z = str(pos[2])
        dim = data.positions[player].get("dimension")
        psi.execute(f'execute in {dim} run tp {player} {x} {y} {z}')
        psi.execute(f'gamemode survival {player}')
        src.reply("已退出旁观模式并返回原位，再次执行此命令以重新开启旁观模式。")
        del data.positions[player]