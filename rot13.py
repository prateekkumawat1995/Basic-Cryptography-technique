#!/usr/bin/env python
import sys
import string
plain = raw_input("Enter plain text : ")
plain = plain.upper()
lookup_table = string.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
cipher=plain.translate(lookup_table)
print("Your Encrypted Text is :"+cipher)
d=raw_input("Do you want to Decrypt (y/n) :")
if d=='y' :
	plain=cipher.translate(lookup_table)
print("Your Decrypted Text is :"+cipher)	  

