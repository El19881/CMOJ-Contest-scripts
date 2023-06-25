p = int(input())
n = int(input())
r = int(input())
infected = n
infected_last = n
day = 0
while infected <= p:
	day += 1
	infected += r*infected_last
	infected_last = infected_last*r
print(day)
