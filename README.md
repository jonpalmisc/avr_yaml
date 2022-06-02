# AVR-YAML

This is an attempt to aggregate and serialize all relevant information about the
AVR architecture into a YAML file. YAML was chosen so that the resulting dataset
is both human- and machine-readable.

## Process

The creation of '[avr.yml](avr.yml)' required a number of steps:

1. Use [Tabula](https://tabula.technology) to extract the summary tables from
   the ISA reference manual.
2. Combine all of the tables into a spreadsheet using
   [Numbers](https://www.apple.com/numbers/).
3. Perform additional formatting to clean up the data and fix errors.
4. Export the data to CSV, found in the 'data' folder.
5. Convert the CSV to a [YAML](https://yaml.org) document using Python.

A copy of the specific AVR reference manual used as part of step (1) is included
in the 'ref' subdirectory. The spreadsheet created in Numbers from step (2) is
not included in this repository.
