password = input()

upper = []
lower = []
digit = []

for letter in password:
	if letter.isupper():
		upper.append(letter)
	elif letter.islower():
		lower.append(letter)
	else:
		digit.append(letter)
		
if len(password) >= 8 and len(password) <= 12 and len(upper)>=2 and len(lower)>=3 and len(digit) >= 1:
	print("Valid")
else:
	print("Invalid")
