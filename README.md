# mat2csv

IOS/IOS XE MAC Address Table to CSV Converter

mat2csv v0.2.3 by Jeremy Drahos
The supported MAC table format is from IOS/IOS-XE.  Example:
Vlan    Mac Address       Type        Ports
  77    0301.3919.829c    DYNAMIC     Gi0/1

Usage: mat2csv.py -i [inputfile] -o [outputfile]
If no arguments are passed, it will be interactive to allow pasting the table, then the csv output will be printed.

You can also use an Ansible dump.  If you use 'ansible -m raw' to 'show mac address-table' across multiple switches at once, saving or pasting that whole output will identify which switch's MAC table it's processing.

