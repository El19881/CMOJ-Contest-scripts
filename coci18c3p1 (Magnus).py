n = input()

words = []

for letter in n:
	if letter == "H" and len(words)==0:
		words.append("H")
	elif letter == "H" and len(words) > 1 and words[len(words)-1] == "I":
		words.append("H")
	elif len(words) >= 1 and letter == "O" and words[len(words)-1] == "H":
			words.append("O")
	elif len(words) >= 1 and letter == "N" and words[len(words)-1] == "O":
			words.append("N")
	elif len(words) >= 1 and letter == "I" and words[len(words)-1] =="N":
			words.append("I")
			
lists = "".join(words)
counter = lists.count("HONI")

print(counter)
