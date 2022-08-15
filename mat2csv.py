# MAC Address Table to CSV v0.2.3 by Jeremy Drahos
# The supported MAC table format is from IOS/IOS-XE
# example:
# Vlan    Mac Address       Type        Ports
#   12    0301.3919.829c    DYNAMIC     Gi0/1
# usage: mat2csv.py -i [inputfile] -o [outputfile]
# if no arguments are passed, it will be interactive to allow pasting the table, then the csv will be printed.

import re
import sys

class mat2csv:
    regex = re.compile(r"\s+(\d+)\s+([0-9a-f]{4}[\.][0-9a-f]{4}[\.][0-9a-f]{4})\s+(\w+)\s+(.+)")
    ansible_regex = re.compile(r"(\S+)\s\|\s(CHANGED)\s\|\s")
    table = []
    switch = ''
    usage = 'usage: mat2csv.py -i [inputfile] -o [outputfile]\nIf no arguments are passed, it will use stdin for you to paste the table, then it will be printed.'
    args = sys.argv[0:]
    infile = ''
    outfile = ''

    def loadfile():
        mat2csv.table = []
        print(f'Loading {mat2csv.infile}...')
        mat2csv.writeheader()
        with open(mat2csv.infile, 'r') as tablefile:
            reader = tablefile.readlines()
            for line in reader:
                mat2csv.writeit(line)
        tablefile.close()
        print(f'{mat2csv.infile} processed...')

    def writeheader():
        print(f'Writing CSV header...')
        with open(mat2csv.outfile, 'w') as initheader:
            initheader.write('switch,vlan,mac,type,if\n')
        initheader.close()
        print(f'Header written to {mat2csv.outfile}...')
        print(f'Writing CSV file, {mat2csv.outfile}...')

    def printit(row):
        ansible_match = re.match(mat2csv.ansible_regex, row)
        matches = re.match(mat2csv.regex, row)
        if ansible_match:
            mat2csv.switch = ansible_match[1]
        if matches:
            print(f'{mat2csv.switch},{matches[1]},{matches[2]},{matches[3]},{matches[4]}')
        
    def writeit(row):
        with open(mat2csv.outfile, 'a') as writefile:
            ansible_match = re.match(mat2csv.ansible_regex, row)
            matches = re.match(mat2csv.regex, row)
            if ansible_match:
                mat2csv.switch = ansible_match[1]
            if matches:
                writefile.writelines(f'{mat2csv.switch},{matches[1]},{matches[2]},{matches[3]},{matches[4]}\n')
        writefile.close()

    def loadcli():
        print('Paste the MAC table output, press return, press ^Z, then press return:\n')
        mat2csv.table = sys.stdin.readlines()
        print('switch,vlan,mac,type,if')
        for line in mat2csv.table:
            mat2csv.printit(line)
        print('Processing complete...')

if len(mat2csv.args) == 1:
    mat2csv.loadcli()
elif mat2csv.args[1] == '-i' and mat2csv.args[3] == '-o':
    mat2csv.infile = mat2csv.args[2]
    mat2csv.outfile = mat2csv.args[4]
    mat2csv.loadfile()
elif mat2csv.args[3] == '-i' and mat2csv.args[1] == '-o':
    mat2csv.infile = mat2csv.args[4]
    mat2csv.outfile = mat2csv.args[2]
    mat2csv.loadfile()
else:
    print(mat2csv.usage)