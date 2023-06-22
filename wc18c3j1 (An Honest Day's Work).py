P = int(input())
B = int(input())
D = int(input())

badges_revenue = (P//B)*D
rest_revenue = (P%B)*1

print(badges_revenue+rest_revenue)
