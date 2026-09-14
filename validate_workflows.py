#!/usr/bin/env python3
"""Validate n8n workflow JSON files in this repo.

Checks, per *.json workflow found next to this script:
  - file is valid JSON with a top-level `nodes` list and `connections` object
  - every node has the required keys (id, name, type, typeVersion, position, parameters)
  - node ids are unique
  - node names are unique (connections reference nodes by name)
  - position is a 2-element numeric list
  - every connection source and target references an existing node name

Prints PASS/FAIL per file and exits non-zero if any file fails.
"""

import glob
import json
import os
import sys

REQUIRED_NODE_KEYS = ("id", "name", "type", "typeVersion", "position", "parameters")


def validate_workflow(path):
    """Return a list of error strings for a single workflow file (empty == OK)."""
    errors = []
    try:
        with open(path, "r", encoding="utf-8") as fh:
            wf = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot parse JSON: {exc}"]

    if not isinstance(wf, dict):
        return ["top-level JSON is not an object"]

    nodes = wf.get("nodes")
    connections = wf.get("connections")

    if not isinstance(nodes, list) or not nodes:
        errors.append("missing or empty `nodes` list")
        nodes = []
    if not isinstance(connections, dict):
        errors.append("missing `connections` object")
        connections = {}

    seen_ids = set()
    node_names = set()

    for idx, node in enumerate(nodes):
        if not isinstance(node, dict):
            errors.append(f"node #{idx} is not an object")
            continue

        label = node.get("name") or node.get("id") or f"#{idx}"

        for key in REQUIRED_NODE_KEYS:
            if key not in node:
                errors.append(f"node '{label}' missing required key '{key}'")

        node_id = node.get("id")
        if node_id is not None:
            if node_id in seen_ids:
                errors.append(f"duplicate node id '{node_id}'")
            seen_ids.add(node_id)

        name = node.get("name")
        if name is not None:
            if name in node_names:
                errors.append(f"duplicate node name '{name}'")
            node_names.add(name)

        pos = node.get("position")
        if pos is not None:
            if (
                not isinstance(pos, list)
                or len(pos) != 2
                or not all(isinstance(c, (int, float)) for c in pos)
            ):
                errors.append(f"node '{label}' has invalid position {pos!r}")

    # Connection integrity: every source and every target must be a known node.
    for source, outputs in connections.items():
        if source not in node_names:
            errors.append(f"connection source '{source}' is not a known node")
        if not isinstance(outputs, dict):
            errors.append(f"connection '{source}' outputs is not an object")
            continue
        for out_type, branches in outputs.items():
            if not isinstance(branches, list):
                errors.append(f"connection '{source}.{out_type}' is not a list")
                continue
            for branch in branches:
                if not isinstance(branch, list):
                    errors.append(
                        f"connection '{source}.{out_type}' branch is not a list"
                    )
                    continue
                for link in branch:
                    target = link.get("node") if isinstance(link, dict) else None
                    if target is None:
                        errors.append(
                            f"connection from '{source}' has a link without a target node"
                        )
                    elif target not in node_names:
                        errors.append(
                            f"connection '{source}' -> unknown node '{target}'"
                        )

    return errors


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    files = sorted(glob.glob(os.path.join(here, "*.json")))
    if not files:
        print("No workflow *.json files found.", file=sys.stderr)
        return 1

    total_nodes = 0
    failed = 0

    for path in files:
        name = os.path.basename(path)
        errors = validate_workflow(path)
        if errors:
            failed += 1
            print(f"FAIL  {name}")
            for err in errors:
                print(f"        - {err}")
        else:
            with open(path, "r", encoding="utf-8") as fh:
                node_count = len(json.load(fh).get("nodes", []))
            total_nodes += node_count
            print(f"PASS  {name}  ({node_count} nodes)")

    passed = len(files) - failed
    print(
        f"\n{passed}/{len(files)} workflow(s) passed, "
        f"{total_nodes} valid node(s) total."
    )
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
