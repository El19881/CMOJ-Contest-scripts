number = int(input())
serve_count = 0
action = ''
taker = 0

while action != "EOF": 
    action = input()
    if action == "TAKE": 
        taker += 1
        if number < 999: 
    	    number += 1 
        else: 
    	    number = 1 
    elif action == "SERVE":
  	    serve_count += 1
    elif action == "CLOSE":
        print(taker, (taker - serve_count), number) 
        serve_count = 0
        taker = 0
