"""Validate source identities and basic fields without deduplicating songs."""
import argparse
import json
from collections import Counter
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    data = json.loads(args.path.read_text(encoding="utf-8-sig"))
    if data.get("schemaVersion") != 1 or not isinstance(data.get("songs"), list):
        raise SystemExit("Invalid schema or song list")
    seen = set()
    games = Counter()
    aliases = 0
    for i, song in enumerate(data["songs"]):
        for key in ("game", "provider", "sourceId", "title"):
            if not isinstance(song.get(key), str) or not song[key].strip():
                raise SystemExit(f"Record {i}: invalid {key}")
        identity = (song["game"], song["provider"], song["sourceId"])
        if identity in seen:
            raise SystemExit(f"Duplicate source identity: {identity}")
        seen.add(identity)
        for key in ("names", "aliases"):
            if not isinstance(song.get(key), list) or not all(isinstance(x, str) and x.strip() for x in song[key]):
                raise SystemExit(f"Record {i}: invalid {key}")
        games[song["game"]] += 1
        aliases += len(song["aliases"])
    print(f"{len(seen)} records, {aliases} aliases")
    for game, count in sorted(games.items()):
        print(f"{game}: {count}")


if __name__ == "__main__":
    main()
