#does not have to be a function, but created as such as the excercise was from the chapter about functions

def check_unique():
	start_year = int(input())
	start_year += 1
	while len(set(str(start_year))) != len(str(start_year)):
		start_year += 1
	print(start_year)

check_unique()
