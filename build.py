#!/usr/bin/env python3

from typing import List, Optional

import csv
import re
import yaml

output = []

def split(s: str, d: str) -> Optional[List[str]]:
    """
    Split a string by a given delimiter. Will return `None` if the input string
    is an empty string.
    """

    if len(s) == 0:
        return None

    return [p.strip() for p in s.split(d)]

with open("data/avr.csv") as file:
    for row in csv.DictReader(file, delimiter=","):
        entry = {}
        entry["id"] = int(row["id"])
        entry["mnem"] = row["mnem"]
        entry["desc"] = row["desc"]
        entry["type"] = row["type"]
        entry["ops"] = split(row["ops"], ',')
        entry["lhs"] = split(row["lhs"], ';')
        entry["op"] = split(row["op"], ';')
        entry["rhs"] = split(row["rhs"], ';')
        entry["pattern"] = row["pattern"]
        entry["flags"] = split(row["flags"], ',')
        entry["words"] = int(row["words"])

        output.append(entry)

output = yaml.dump(output, sort_keys=False)
output = re.sub(r'^-', '\n-', output, flags=re.MULTILINE)
output = "\n".join(output.splitlines()[1:])

print(output)
