# Rhythm Song Catalog

一个整理多款音游曲名、曲师和部分别名的数据项目，提供 JSON 文件供检索、匹配和开发使用。

## 曲库

完整整理快照：[`data/catalog.json`](data/catalog.json)，包含 5870 条来源记录，覆盖 Arcaea、Phigros、Project SEKAI、BanG Dream!、maimai、CHUNITHM、Rotaeno、Milthm 和 Rizline。部分歌曲附有别名；ASTRODX 按 maimai 归类。

另有独立的 [`data/arcaea.json`](data/arcaea.json)，包含 544 条 Arcaea 曲目及 817 个别名。

这些数字是**来源记录数，而不是去重后的歌曲数**。同一首联动曲在多个游戏中可以分别出现，同名也不一定代表同一首歌。曲库不是完整性保证；服务器、更新时间及来源说明见 [SOURCES.md](SOURCES.md)。

**数据质量提示：** 部分 Wiki 提取结果仍存在重复来源 ID 和格式残留，别名也未经逐条核实。全量快照可用于研究和测试，但使用前应按需求清洗；不要把它视为准确无误的官方数据。

**许可提示：** 各来源的使用和再分发条件不尽相同，部分尚未确认。Arcaea Toolbelt 上游仓库标注 MIT，许可证保存在 [`licenses/`](licenses/)；这不代表所有来源数据、歌曲或相关素材均使用相同许可。使用或再分发前请自行核实各来源及相关权利。

## 数据格式

每个 JSON 文件包含 `schemaVersion`、`sources` 和 `songs`。曲目示例：

```json
{
  "game": "arcaea",
  "provider": "arcaea-toolbelt",
  "sourceId": "sayonarahatsukoi",
  "title": "Sayonara Hatsukoi",
  "artist": "REDSHiFT",
  "names": ["Sayonara Hatsukoi"],
  "aliases": ["再见初恋", "失恋", "再见世征"]
}
```

`names` 保存来源中的正式名或本地化名称，`aliases` 保存已收集的别名。`game`、`provider`、`sourceId` 共同标识来源记录；现有全量快照中部分记录尚未满足唯一性要求。

## 调用

可以下载 JSON 文件并在本地读取，或通过 GitHub 的 Raw 文件地址获取。生产环境建议固定 Git 提交版本并缓存文件，避免依赖实时网络和数据变动。

Python 示例：

```python
import json
from pathlib import Path

catalog = json.loads(Path("data/catalog.json").read_text(encoding="utf-8"))
matches = [
    song for song in catalog["songs"]
    if "Aegleseeker" in [song["title"], *song["names"], *song["aliases"]]
]
print(matches)
```

数据中有跨游戏重复，建议根据应用场景先筛选 `game`，再搜索其余游戏。别名可能有歧义，不应假定其全局唯一。

## 校验和贡献

使用 Python 3.9 或更新版本，无第三方依赖：

```sh
python tools/validate.py data/arcaea.json
python tools/validate.py data/catalog.json
```

校验器检查必填字段和来源 ID 唯一性；全量快照目前已知会报告重复，待清洗。欢迎提交来源、错误修正和别名，并注明依据及数据许可；请勿提交私人截图、音频、曲绘或谱面。
