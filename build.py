#!/usr/bin/env python3

from numbers_parser import Document
import pandas as pd
import yaml

import re
import sys


def encoding_to_mask(encoding: str) -> int:
    m = 0
    for c in encoding:
        m <<= 1
        if c == "1" or c == "0":
            m |= 1
    return m


def encoding_to_pattern(encoding: str) -> int:
    t = 0
    for c in encoding:
        t <<= 1
        if c == "1" or c == "0":
            t |= 1 if c == "1" else 0
    return t


def encoding_to_constraint(encoding: str) -> str:
    k = ""
    for c in encoding:
        if c == "1" or c == "0":
            k += "-"
        else:
            k += c
    return k


if len(sys.argv) < 2:
    sys.exit(1)

doc = Document(sys.argv[1])
data = doc.sheets[0].tables[0].rows(values_only=True)
df = pd.DataFrame(data[1:], columns=data[0])

output = []

for i, row in df.iterrows():
    e = {}
    e["id"] = i
    e["mnemonic"] = row["mnemonic"]
    e["description"] = row["description"]
    e["operands"] = [o.strip() for o in (row["operands"] or "").split(",")]

    e["variant"] = row["variant"]
    e["lhs"] = (row["lhs"] or "").splitlines()
    e["op"] = row["op"]
    e["rhs"] = (row["rhs"] or "").splitlines()

    e["flags"] = [c for c in (row["flags"] or "")]

    e["encoding"] = row["encoding"]
    e["mask"] = encoding_to_mask(e["encoding"])
    e["pattern"] = encoding_to_pattern(e["encoding"])
    e["constraint"] = encoding_to_constraint(e["encoding"])
    e["width"] = row["width"]

    e["cycles"] = {
        "e": row["avr_e"],
        "xm": row["avr_xm"],
        "xt": row["avr_xt"],
        "rc": row["avr_rc"],
    }

    output.append(e)

output = yaml.dump(output, sort_keys=False)
output = re.sub(r"^-", "\n-", output, flags=re.MULTILINE)
output = "\n".join(output.splitlines()[1:])

print(output)
