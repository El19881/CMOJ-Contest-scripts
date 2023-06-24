number = int(input())
list_words = []

for n in range (number):
	text = input().lower()
	list_words.append(text)

string_words = " ".join(list_words)

counter_s = string_words.count("s")
counter_t = string_words.count("t")

if counter_s > counter_t:
	print("French")
elif counter_s < counter_t:
	print("English")
else:
	print("French")
