value = input()
happy = 0
sad = 0

for i in range(0,len(value)):
    if value[i] == ":":
        if i+1<len(value):
            if value[i+1] == "-":
                if i+2<len(value):
                    if value[i+2] == ")":
                        happy += 1
                    elif value[i+2] == "(":
                        sad += 1

        
if happy == sad and happy != 0 and sad != 0:
    print('unsure')
if happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
elif happy == sad == 0:
    print('none')
