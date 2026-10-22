"""Validate a flat accelerator config and optionally emit GitHub Actions outputs."""

from __future__ import annotations

import os
import sys
from pathlib import Path

REQUIRED_KEYS = ("name", "workflow", "runtime", "version", "install", "lint", "test")
WORKFLOWS = {"library", "service", "web", "data-pipeline", "tool"}
IMPLEMENTED = {("library", "python")}


def parse_config(text: str, source: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line_number, raw in enumerate(text.splitlines(), start=1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith((" ", "\t")) or raw.lstrip().startswith("-"):
            raise SystemExit(f"{source}:{line_number}: use flat key: value entries")
        if ":" not in raw:
            raise SystemExit(f"{source}:{line_number}: expected key: value")
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        if not key or not value:
            raise SystemExit(f"{source}:{line_number}: key and value are required")
        data[key] = value
    return data


def validate_config(path: Path) -> dict[str, str]:
    data = parse_config(path.read_text(encoding="utf-8"), str(path))
    missing = [key for key in REQUIRED_KEYS if key not in data]
    if missing:
        raise SystemExit(f"{path}: missing {', '.join(missing)}")
    folder = path.parent.name
    if data["name"] != folder:
        raise SystemExit(f"{path}: name must match the folder '{folder}'")
    if data["workflow"] not in WORKFLOWS:
        raise SystemExit(f"{path}: unknown workflow '{data['workflow']}'")
    pair = (data["workflow"], data["runtime"])
    if pair not in IMPLEMENTED:
        raise SystemExit(
            f"{path}: {data['workflow']} for {data['runtime']} is not implemented yet"
        )
    return data


def write_github_output(data: dict[str, str]) -> None:
    github_output = os.environ.get("GITHUB_OUTPUT")
    if not github_output:
        raise SystemExit("GITHUB_OUTPUT is not set")
    with Path(github_output).open("a", encoding="utf-8") as handle:
        for key in REQUIRED_KEYS:
            handle.write(f"{key}={data[key]}\n")


def main(argv: list[str]) -> None:
    if len(argv) < 2:
        raise SystemExit("usage: read_config.py <config.yml> [--github-output]")
    data = validate_config(Path(argv[1]))
    if "--github-output" in argv:
        write_github_output(data)
    else:
        print(f"{data['name']}: {data['workflow']} ({data['runtime']} {data['version']})")


if __name__ == "__main__":
    main(sys.argv)
