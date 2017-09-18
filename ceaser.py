#!/usr/bin/env python

import sys

# choose your option

while true:
	d=input("*******Ceaser Cipher************\nChoose your option:\n1. Encryption \n2. Decryption\n3. Exit ")
	
	# Encrytion of plain text

	if d=='1':
		plain = raw_input("Enter plain text : ")
		plain = plain.replace(" ", "")
		plain = plain.upper()
		s = list(plain)
		k = input("Enter encryption key : ")
		
		for i in s:
			i = chr(((ord(i)-64+k)%26)+64)
		print("Encrypted cipher text is =".join(s))

	# Decryption of cipher text

	if d=='y' :
		plain = raw_input("Enter encrypted text : ")
		plain = plain.replace(" ", "")
		plain = plain.upper()
		s = list(plain)
		print("Choose your suitable text from the given possibilities")
		# -----------------------------------------	
		for i in s:
			a = ord(s[x])-(64+k)
			if a<=0 :
				a=a+26
			a=a+64
			s[x] = chr(a)
			x=x+1
		print("".join(s))		
		# --------------------------------------------- 
