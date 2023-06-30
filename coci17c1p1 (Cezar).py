cezar_drawn = int(input())
cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]
card_list = []
deal = 0
no_deal = 0

for i in range(cezar_drawn):
	value = int(input())
	card_list.append(value)
total_cezar = sum(card_list)


for i in card_list:
	if i in cards:
		cards.remove(i)

for i in cards:
	if i + total_cezar > 21:
		no_deal+=1
	elif i + total_cezar <= 21:
		deal +=1

if deal>no_deal:
	print("VUCI")
elif no_deal>=deal:
	print("DOSTA")
