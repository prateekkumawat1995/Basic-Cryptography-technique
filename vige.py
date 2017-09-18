#!/usr/bin/env python
import sys
plain = raw_input("Enter plain text : ")
plain = plain.replace(" ", "")
plain = plain.upper()
s = list(plain)
plain = raw_input("Enter your key : ")
k = list(plain)
x=0
y=0
length = len(k);
for i in s:
	a = ord(s[x])
	b = ord(k[y])
	s[x] = chr(((a+b-128)%26)+64)
	x=x+1
	y=y+1
	if y==length:
		y=0	
print("".join(s))
x=0
y=0
d=raw_input("Do you want to Decrypt (y/n) :")
if d=='y' :
	for i in s:
		a = ord(s[x])
		b = ord(k[y])
		if(a-b<=0):
			a=a+26
		s[x] = chr(a-b+64)
		x=x+1
		y=y+1
		if y==length:
			y=0	
print("".join(s))
		 
