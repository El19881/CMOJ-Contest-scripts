number = int(input())
readings = input()

readings_list = readings.split(" ")
integers = [int(x) for x in readings_list]

min = min(integers)
max = max(integers)

min_index = integers.index(min)
max_index = integers.index(max)

new_list = integers[min_index:max_index+1]
result = []
if min_index>max_index:
    result.append(False)
for i in range(len(new_list)):
	if new_list[i] != new_list[-1] and new_list[i] < new_list[i+1]:
		result.append(True)
	elif new_list[i] == new_list[-1]:
		result.append(True)
	else:
		result.append(False)

if False in result:
	print("unknown")
else: 
	print(max-min)
