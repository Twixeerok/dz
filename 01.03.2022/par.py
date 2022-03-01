
import time
import random

def gen(s,b):
    while True:
        a = random.randrange(s,b)
        yield a
        time.sleep(0.5)
        s += 10
        b += 10

a = gen(1,10)
for i in a:
    print(i)

import sys
import argparse
import csv

s = []
print(sys.argv)
parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name',
required=True)
parser.add_argument('-ln', '--last-name',
required=True)
parser.add_argument('-y', '--years',
required=True)
parser.add_argument('echo')
args = parser.parse_args()
print(args)
print('First name:', args.first_name)
print('Last name:', args.last_name)
print('years:', args.years)
s.append(args)

with open('a.csv', 'w') as file:
    a = csv.writer(file)
    a.writerow(s)
