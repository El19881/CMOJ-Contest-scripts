number = int(input())
list_info = []
counter = 0

for i in range(number*2):
	info = input()
	list_info.append(info)

questions = list_info[0:number]
answers = list_info[number:]

for i in range(len(questions)):
	if questions[i] == answers[i]:
		counter+=1

print(counter)
