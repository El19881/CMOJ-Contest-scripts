opened = int(input())
opened_list = []

for i in range(opened):
	value = int(input())
	opened_list.append(value)
	
banker = int(input())

total = 1691600
counter = 0
for i in opened_list:
	if i == 1:
		total -= 100
	elif i == 2:
		total -= 500
	elif i == 3:
		total -= 1000
	elif i == 4:
		total -= 5000
	elif i == 5:
		total -= 10000
	elif i == 6:
		total -= 25000
	elif i == 7:
		total -= 50000
	elif i == 8:
		total -= 100000
	elif i == 9:
		total -= 500000
	elif i == 10:
		total -= 1000000
	counter+=1

new_total = total/(10-counter)

if new_total>banker:
	print("no deal")
else:
	print("deal")
