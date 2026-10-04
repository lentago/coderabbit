#!/usr/bin/env python3
"""Validate .coderabbit.yaml against CodeRabbit's published schema.

The schema is fetched at run time (https://coderabbit.ai/integrations/schema.v2.json)
so the check tracks CodeRabbit's current options; a network failure is reported
as such rather than passed. Exit 0 on valid, 1 on invalid or unreachable.
"""
import json
import sys
import urllib.request

try:
    import yaml
    import jsonschema
except ImportError as exc:  # pragma: no cover
    print(f"missing dependency: {exc.name} (pip install pyyaml jsonschema)", file=sys.stderr)
    sys.exit(1)

SCHEMA_URL = "https://coderabbit.ai/integrations/schema.v2.json"

def main() -> int:
    try:
        with urllib.request.urlopen(SCHEMA_URL, timeout=30) as r:
            schema = json.load(r)
    except Exception as exc:
        print(f"could not fetch the CodeRabbit schema: {exc}", file=sys.stderr)
        return 1
    with open(".coderabbit.yaml", encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh)
    errors = sorted(jsonschema.Draft202012Validator(schema).iter_errors(cfg), key=lambda e: list(e.path))
    for e in errors:
        print(f"INVALID at {'/'.join(str(p) for p in e.path) or '$'}: {e.message}")
    if errors:
        return 1
    print(".coderabbit.yaml is valid against the current CodeRabbit schema")
    return 0

if __name__ == "__main__":
    sys.exit(main())
