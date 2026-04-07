#!/usr/bin/env python3
"""Validate SC Evo wiki markup output against structural rules and entities.json."""

import json
import re
import sys
from pathlib import Path

VALID_PREFIXES = ("User:SCEvo/SCAbility/", "User:SCEvo/SCUpgrade/", "User:SCEvo/")
COLOR_TAGS = re.compile(r"%(red|green|yellow)%|%%")
BRACKET_GAME_SPEED = re.compile(r"\[\s*[\d.+]+\s*→\s*[\d.+]+\s*\]")
WIKI_LINK = re.compile(r"\[\[([^|\]]+)\|([^\]]+)\]\]")
WRONG_ARROW = re.compile(r"(?<!<)--?>")  # matches -> and --> but not HTML comments
BULLET_DEPTH = re.compile(r"^(\*+)")


def load_entities(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def slug_from_path(link_path: str) -> tuple[str, str]:
    """Return (entity_type, slug) from a wiki link path.

    e.g. 'User:SCEvo/SCUpgrade/Grooved Spines' -> ('upgrades', 'Grooved Spines')
         'User:SCEvo/Vulture' -> ('units', 'Vulture')
    """
    if link_path.startswith("User:SCEvo/SCAbility/"):
        return "abilities", link_path[len("User:SCEvo/SCAbility/"):]
    if link_path.startswith("User:SCEvo/SCUpgrade/"):
        return "upgrades", link_path[len("User:SCEvo/SCUpgrade/"):]
    if link_path.startswith("User:SCEvo/"):
        return "units", link_path[len("User:SCEvo/"):]
    return "unknown", link_path


DELIMITERS = {"(": ")", "[": "]", "{": "}"}
CLOSERS = set(DELIMITERS.values())


def check_balanced_delimiters(line: str, line_num: int, errors: list):
    """Check that (), [], {} are balanced on a single line.

    Wiki links [[...]] and templates {{...}} use doubled delimiters —
    we count individual characters so a missing closer is still caught.
    """
    # Consume wikitable tokens ({|, |}) before brace counting; they are
    # tracked separately at the file level via check_wikitable_balance.
    line = line.replace("{|", "").replace("|}", "")
    stack = []
    for ch in line:
        if ch in DELIMITERS:
            stack.append((ch, DELIMITERS[ch]))
        elif ch in CLOSERS:
            if stack and stack[-1][1] == ch:
                stack.pop()
            else:
                errors.append(
                    f"L{line_num}: unexpected closing '{ch}': {line.strip()}"
                )
                return
    if stack:
        unclosed = "".join(pair[0] for pair in stack)
        errors.append(
            f"L{line_num}: unclosed delimiter(s) '{unclosed}': {line.strip()}"
        )


def detect_mode(lines: list[str]) -> str:
    """Detect whether the output is Mode A (changelog) or Mode B (per-unit wikitable)."""
    for line in lines:
        if line.strip().startswith("{| class=\"wikitable"):
            return "B"
        if line.strip().startswith("* Versus"):
            return "A"
    return "unknown"


def validate_mode_a(lines: list[str], entities: dict) -> tuple[list, list, list]:
    """Validate Mode A (patch changelog) output."""
    errors = []
    warnings = []
    info = []

    seen_depths = set()
    entity_resolutions: dict[str, list[str]] = {}  # name -> [type, type, ...]
    unknown_entities = []

    for i, raw_line in enumerate(lines, 1):
        line = raw_line.rstrip()
        if not line:
            continue

        # --- Hard errors ---

        # Color tags
        if COLOR_TAGS.search(line):
            errors.append(f"L{i}: surviving color tag: {line.strip()}")

        # Balanced delimiters
        check_balanced_delimiters(line, i, errors)

        # Bracketed game-speed values
        if BRACKET_GAME_SPEED.search(line):
            errors.append(f"L{i}: surviving bracketed game-speed value: {line.strip()}")

        # Wrong arrow
        if WRONG_ARROW.search(line):
            errors.append(f"L{i}: wrong arrow (use →): {line.strip()}")

        # Bullet depth hierarchy
        m = BULLET_DEPTH.match(line)
        if m:
            depth = len(m.group(1))
            seen_depths.add(depth)
            if depth == 4 and 3 not in seen_depths:
                errors.append(f"L{i}: **** without preceding ***: {line.strip()}")
            if depth == 3 and 2 not in seen_depths:
                errors.append(f"L{i}: *** without preceding **: {line.strip()}")
            if depth == 2 and 1 not in seen_depths:
                errors.append(f"L{i}: ** without preceding *: {line.strip()}")

        # Wiki link validation
        for link_match in WIKI_LINK.finditer(line):
            link_path = link_match.group(1)
            display = link_match.group(2)

            # Must start with a valid prefix
            if not any(link_path.startswith(p) for p in VALID_PREFIXES):
                errors.append(
                    f"L{i}: invalid link prefix: [[{link_path}|{display}]]"
                )
                continue

            etype, slug = slug_from_path(link_path)

            # Check against entities.json
            section = entities.get(etype, {})
            # Check by slug match (value could match any key's slug)
            known = any(
                entry.get("slug") == slug for entry in section.values()
            )
            # Also check by key name
            if not known:
                known = slug in section

            if not known:
                warnings.append(
                    f"L{i}: entity not in entities.json: {etype}/{slug}"
                )
                unknown_entities.append(f"{etype}/{slug}")

            # Track ambiguous name resolution
            # Find if this name exists in multiple entity sections
            name = slug
            sections_with_name = []
            for sname in ("units", "abilities", "upgrades"):
                sec = entities.get(sname, {})
                if name in sec or any(
                    e.get("slug") == name for e in sec.values()
                ):
                    sections_with_name.append(sname)

            if len(sections_with_name) > 1:
                entity_resolutions.setdefault(name, []).append(etype)

        # Check for malformed wiki links (unmatched brackets)
        bracket_count = line.count("[[")
        if bracket_count != line.count("]]"):
            errors.append(f"L{i}: mismatched wiki link brackets: {line.strip()}")

    # --- Warnings: ambiguous name resolution ---
    for name, resolutions in entity_resolutions.items():
        unique = set(resolutions)
        if len(resolutions) > 1 and len(unique) == 1:
            warnings.append(
                f"ambiguous entity '{name}' resolved as {unique.pop()} "
                f"every time ({len(resolutions)} occurrences) — verify this is correct"
            )
        else:
            info.append(
                f"ambiguous entity '{name}' resolved as: "
                + ", ".join(resolutions)
            )

    # --- Info: unknown entities ---
    if unknown_entities:
        info.append(
            f"entities not in entities.json (add if valid): "
            + ", ".join(sorted(set(unknown_entities)))
        )

    return errors, warnings, info


def validate_mode_b(lines: list[str], entities: dict) -> tuple[list, list, list]:
    """Validate Mode B (per-unit wikitable) output."""
    errors = []
    warnings = []
    info = []

    has_table_open = False
    has_table_close = False
    has_citation = False
    table_depth = 0

    for i, raw_line in enumerate(lines, 1):
        line = raw_line.rstrip()
        if not line:
            continue

        # Color tags
        if COLOR_TAGS.search(line):
            errors.append(f"L{i}: surviving color tag: {line.strip()}")

        # Balanced delimiters
        check_balanced_delimiters(line, i, errors)

        # Bracketed game-speed values
        if BRACKET_GAME_SPEED.search(line):
            errors.append(f"L{i}: surviving bracketed game-speed value: {line.strip()}")

        # Wrong arrow (in Mode B values use "from X to Y" but raw arrows could survive)
        if WRONG_ARROW.search(line):
            errors.append(f"L{i}: wrong arrow (use →): {line.strip()}")

        # Table structure: track {| / |} balance across lines
        opens = line.count("{|")
        closes = line.count("|}")
        if opens:
            has_table_open = True
            table_depth += opens
        if closes:
            table_depth -= closes
            if table_depth >= 0:
                has_table_close = True
            if table_depth < 0:
                errors.append(f"L{i}: unexpected wikitable close '|}}' with no matching '{{|'")
                table_depth = 0
        if "<ref>" in line and "Cite web" in line:
            has_citation = True

            # Validate citation structure
            cite_match = re.search(r"\{\{Cite web\|([^}]*)\}\}", line)
            if not cite_match:
                errors.append(f"L{i}: malformed citation — check Cite web template fields")
            else:
                fields = dict(
                    part.split("=", 1)
                    for part in cite_match.group(1).split("|")
                    if "=" in part
                )
                allowed = ("url", "title", "author", "publisher", "date")
                missing = [f for f in allowed if f not in fields]
                extra = [f for f in fields if f not in allowed]
                if missing:
                    errors.append(
                        f"L{i}: citation missing field(s): {', '.join(missing)}"
                    )
                if extra:
                    errors.append(
                        f"L{i}: citation has disallowed field(s): {', '.join(extra)}"
                    )
                url = fields.get("url", "")
                date = fields.get("date", "")
                if not url:
                    warnings.append(f"L{i}: empty URL in citation")
                if not date:
                    warnings.append(f"L{i}: empty date in citation")

        # Check for MISSING metadata comments
        if "<!-- MISSING:" in line:
            warnings.append(f"L{i}: missing metadata: {line.strip()}")

        # Wiki link validation (Mode B can still have links in prose)
        for link_match in WIKI_LINK.finditer(line):
            link_path = link_match.group(1)
            display = link_match.group(2)
            if not any(link_path.startswith(p) for p in VALID_PREFIXES):
                errors.append(f"L{i}: invalid link prefix: [[{link_path}|{display}]]")

    if not has_table_open:
        errors.append("missing wikitable opening: {| class=\"wikitable ...\"")
    if not has_table_close:
        errors.append("missing wikitable closing: |}")
    if table_depth > 0:
        errors.append(f"unclosed wikitable(s): {table_depth} '{{|' without matching '|}}'")
    if not has_citation:
        warnings.append("no citation/ref found in table header")

    return errors, warnings, info


def main():
    # Determine input source
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])
        if not input_path.exists():
            print(f"[ERROR] File not found: {input_path}", file=sys.stderr)
            sys.exit(2)
        text = input_path.read_text()
    else:
        text = sys.stdin.read()

    # Load entities.json from same directory as this script
    script_dir = Path(__file__).resolve().parent
    entities_path = script_dir / "entities.json"
    if not entities_path.exists():
        print(f"[ERROR] entities.json not found at {entities_path}", file=sys.stderr)
        sys.exit(2)

    entities = load_entities(entities_path)
    lines = text.splitlines()

    mode = detect_mode(lines)
    if mode == "A":
        errors, warnings, info = validate_mode_a(lines, entities)
    elif mode == "B":
        errors, warnings, info = validate_mode_b(lines, entities)
    else:
        print("[ERROR] could not detect output mode (A: changelog or B: wikitable)")
        sys.exit(2)

    # Report
    for msg in errors:
        print(f"[ERROR] {msg}")
    for msg in warnings:
        print(f"[WARN]  {msg}")
    for msg in info:
        print(f"[INFO]  {msg}")

    total = len(errors) + len(warnings)
    if not total and not info:
        print(f"[OK] Mode {mode} output validated — no issues found.")

    # Exit code: 2 for errors, 1 for warnings only, 0 for clean
    if errors:
        sys.exit(2)
    elif warnings:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
