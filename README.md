# mat2csv

IOS/IOS XE MAC Address Table to CSV Converter

mat2csv v0.2.1 by Jeremy Drahos
The supported MAC table format is from IOS/IOS-XE.  Example:
Vlan    Mac Address       Type        Ports
  77    0301.3919.829c    DYNAMIC     Gi0/1

Usage: mat2csv.py -i [inputfile] -o [outputfile]
If no arguments are passed, it will be interactive to allow pasting the table, then the csv output will be printed.
