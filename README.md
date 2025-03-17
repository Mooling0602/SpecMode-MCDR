# SpecMode-MCDR
[MCDR](https://mcdreforged.com)插件[Gamemode](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/gamemode)的精简版本。

移除了一些用处不大且和其他插件发生冲突的命令，仅保留核心的旁观模式切换功能。

## 依赖
- [Minecraft Data API](https://github.com/Fallen-Breath/MinecraftDataAPI)
> 用于记录玩家所处位置，方便快速返回

- [OnlinePlayerAPI](https://github.com/AnzhiZhang/MCDReforgedPlugins/tree/master/src/online_player_api)
> 用于在控制台执行命令时检测玩家是否在线

# 用法
在控制台执行`!!spec <player>`，或由玩家执行`!!spec`，用于切换成旁观模式或切换回生存模式并返回原位
> `<player>`参数为玩家的游戏名
>
> 若需要更多功能，考虑使用原插件。
