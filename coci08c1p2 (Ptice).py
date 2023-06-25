number_questions = int(input())
answers = input()
adrian = 'ABC'
bruno = 'BABC'
goran = 'CCAABB'
score_adrian = 0
score_bruno = 0
score_goran = 0
for i in range(number_questions):
    if answers[i] == adrian[i % 3]:
        score_adrian += 1
    if answers[i] == bruno[i % 4]:
        score_bruno += 1
    if answers[i] == goran[i % 6]:
        score_goran += 1
max_number = max(score_adrian, score_bruno, score_goran)
print(max_number)
if score_adrian == max_number:
    print("Adrian")
if score_bruno == max_number:
    print("Bruno")
if score_goran == max_number:
    print("Goran")
