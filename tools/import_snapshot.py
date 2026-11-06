"""Convert a Rhythm Album snapshot to the public catalogue schema."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = json.loads(args.input.read_text(encoding="utf-8-sig"))
    songs = []
    for row in source["songs"]:
        songs.append({
            "game": row["game"],
            "provider": row["provider"],
            "sourceId": str(row["sourceId"]),
            "title": row["title"],
            "artist": row.get("artist") or "",
            "names": row.get("names") or [],
            "aliases": row.get("aliases") or [],
        })
    output = {
        "schemaVersion": 1,
        "sources": source.get("sources", []),
        "songs": songs,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(output, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"Wrote {len(songs)} records to {args.output}")


if __name__ == "__main__":
    main()
