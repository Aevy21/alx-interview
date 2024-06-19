# Log Parser

This project contains a Python script that reads logs from standard input line by line and computes the following metrics:
- Total file size from all logs
- Number of occurrences of specific HTTP status codes

## Usage

To run the script, provide input through standard input. The script will process the input and print the statistics.

```bash
cat log.txt | ./log_parser.py

## Requirements
Ubuntu 20.04 LTS
Python 3.4.3
PEP 8 style guide (version 1.7.x)
## Script Structure
log_parser.py: The main script
## PEP 8
The code follows the PEP 8 style guide for Python.

## File Length
The script's length can be tested using the wc command.


Make sure the script is executable by running:
```bash
chmod +x log_parser.py

