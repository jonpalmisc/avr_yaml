#!/bin/bash

TAB=$'\t'
NL=$'\t'

REGEX+='^6.[0-9]+\s(\w+)(.|\n)*?'          # Instruction section start and name
REGEX+='([0-9]+).bit Opcode:((.|\n)*?)6\.' # Opcode table through next section

rg -U "$REGEX" -or "\$1$TAB\$3\$4$NL" |
	rg -v -e '2021 Microchip Technology' -e 'Instruction Description'
