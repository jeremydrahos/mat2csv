# mat2csv

IOS/IOS XE MAC Address Table to CSV Converter

mat2csv v0.2.3 by Jeremy Drahos
<br>
The supported MAC table format is from IOS/IOS-XE.

Example:
<br>
```
Vlan    Mac Address       Type        Ports
  77    0301.3919.829c    DYNAMIC     Gi0/1
```
<br>

Usage: ``` mat2csv.py -i [inputfile] -o [outputfile] ```

<br>
If no arguments are passed, it will be interactive to allow pasting the table, then the csv output will be printed.
<br>
You can also use an Ansible dump.

```ansible -m raw "show mac address-table"``` across multiple switches at once, saving or pasting that whole output will identify which switch's MAC table it's processing.

