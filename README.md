# Rhythm Song Catalog

用于整理音游歌曲名称和部分别名的独立曲库项目。数据保留游戏和上游来源，不按同名自动合并歌曲；ASTRODX 使用 maimai 曲库，不作为独立游戏。

## 当前公开数据

`data/arcaea.json` 包含 Arcaea Toolbelt 6.16.1c 快照的 544 条曲目，部分曲目包含社区别名。数据来自 [Arcaea Toolbelt Data](https://github.com/DarrenDanielDay/arcaea-toolbelt-data)，上游仓库标注 MIT，许可证全文在 `licenses/arcaea-toolbelt-MIT.txt`。歌曲标题、艺术家名称等内容的权利可能另属于相应权利人；不包含音频、曲绘或谱面。

其他来源的再分发许可尚未确认，**不在公开仓库中提供数据**。已有的本地研究快照包含 Phigros、Project SEKAI 日服、BanG Dream!、maimai、CHUNITHM、Rotaeno、Milthm 和 Rizline；条目完整性及来源许可还需逐一核对，不能称为完整官方曲库。

## 数据格式

```json
{
  "schemaVersion": 1,
  "sources": [{"game": "arcaea", "provider": "arcaea-toolbelt", "revision": "...", "license": "MIT"}],
  "songs": [
    {
      "game": "arcaea",
      "provider": "arcaea-toolbelt",
      "sourceId": "sayonarahatsukoi",
      "title": "Sayonara Hatsukoi",
      "artist": "REDSHiFT",
      "names": ["Sayonara Hatsukoi"],
      "aliases": ["再见初恋", "失恋", "再见世征"]
    }
  ]
}
```

`names` 是正式名或本地化名称，`aliases` 是来源提供的别名；别名不保证准确、唯一或覆盖全部曲目。`game + provider + sourceId` 构成来源记录的身份，同一作品跨游戏可能有多条记录。

## 本地整理

需要 Python 3.9 或更新版本，无第三方依赖。可把个人已有的 Rhythm Album 曲库快照转换为统一格式：

```sh
python tools/import_snapshot.py --input PATH_TO_SNAPSHOT --output local/catalog.json
python tools/validate.py local/catalog.json
python tools/validate.py data/arcaea.json
```

导入不会修改输入文件，输出已存在时会拒绝覆盖。`local/` 被 Git 忽略，不会因为运行命令而提交许可未确认的数据。上游数据可能变化，公开发布任何额外数据前请先核查每个来源的再分发条件、署名要求及真实性。

## 状态与贡献

来源与待办见 [SOURCES.md](SOURCES.md)。欢迎补充可验证的公开数据源和许可信息；提交别名时请说明对应歌曲和依据，勿上传个人截图或其他私人数据。请勿将歌曲、谱面和曲绘的权利等同于数据整理脚本的许可。
