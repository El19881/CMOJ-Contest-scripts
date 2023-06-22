a_3_point = int(input())
a_2_point = int(input())
a_1_point = int(input())
b_3_point = int(input())
b_2_point = int(input())
b_1_point = int(input())

a_Score = a_3_point*3 + a_2_point*2 + a_1_point
b_Score = b_3_point*3 + b_2_point*2 + b_1_point

if a_Score > b_Score:
    print("A")
elif a_Score < b_Score:
    print("B")
else:
    print("T")
