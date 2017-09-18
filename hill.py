#!/usr/bin/env python
import sys
from math import sqrt
from numpy import matrix
plain = raw_input("Enter plain text : ")
plain = plain.replace(" ", "")
plain = plain.upper()
key = raw_input("Enter plain key : ")
n = int(sqrt(len(key)))
    if n * n != len(key):
        raise Exception("Invalid key length")
if len(plain)%n > 0:
	plain += '|' * (n - (len(plain) % n))
