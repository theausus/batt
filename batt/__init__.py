#!/usr/bin/python3
import os
def main():
    now, full, path = [], [], '/sys/class/power_supply/'
    if os.path.exists('{}/.battrc'.format(os.path.expanduser('~'))):
        path = open('{}/.battrc'.format(os.path.expanduser('~'))).read()
    for d in os.listdir(path):
       if d != 'AC':
            f_now = open('{}/{}/charge_now'.format(path, d))
            f_full = open('{}/{}/charge_full'.format(path, d))
            now.append(int(f_now.read()[:-1]))
            full.append(int(f_full.read()[:-1]))
            f_now.close()
            f_full.close()
    now, full = sum(now), sum(full)
    if full:
        print(now, 'of', full, 'mWh')
        print(round((now / full)* 100, 2), '%', sep='')
