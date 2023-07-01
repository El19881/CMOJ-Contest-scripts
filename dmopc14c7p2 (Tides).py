n_numbers = int(input())
#the below also works insted of lines 4-6:
#list_numbers = list(map(int,input().split()))
list_numbers = input()
list_numbers = list_numbers.split(" ")
list_numbers = [int(i) for i in list_numbers]

min, max = min(list_numbers), max(list_numbers)
min_i, max_i = list_numbers.index(min), list_numbers.index(max)

new_list = list_numbers[min_i:max_i+1]

if new_list != sorted(new_list) or min_i>max_i:
	print("unknown")
else:
	print(max-min)
