#!/usr/bin/env python3

from pypdf import PdfReader

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("pdf")
parser.add_argument("-s", "--start", default=0)
parser.add_argument("-e", "--end", default=None)

args = parser.parse_args()

reader = PdfReader(args.pdf)

start_page = args.start
if end_page := args.end:
    page_range = reader.pages[start_page:end_page]
else:
    page_range = reader.pages[start_page:]

for p in page_range:
    print(p.extract_text())
