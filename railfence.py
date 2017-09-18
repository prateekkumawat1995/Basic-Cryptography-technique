#!/usr/bin/env python
import sys
rails = int(input("Enter the number of layers: "))
plain_text = raw_input("Enter the plain text: ")
plain_text = plain_text.replace(" ", "")
plain_text = plain_text.upper()
length=len(plain_text)
rail = [""] * rails
r = 0
for c in plain_text:
	rail[r] += c
	if(r>=rails-1):
		r=0
	else:
		r+=1
cipher = "".join(rail)
print("Your Encrypted Text is :"+cipher)  
d=raw_input("Do you want to Decrypt (y/n) :")
if d=='y' :
	ciph = [""] * rails
	r=0
	nor=rails
	for c in reversed(cipher):
		  ciph[r] += c
		  nor=nor-1
		  if(nor==0):
		  	r=r+1
		  	nor=(rails*2)
		  if(r==(rails-1)):
		  	nor==(rails+1)
	r=0	  	
	pos=0
	cipher=[""]
	while pos<length:
		 
				  	
