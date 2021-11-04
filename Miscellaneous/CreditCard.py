card_list = []
buyers = []
bounce_rate = []


for _ in range(4):
    lst = input().split()
    card_list.append(lst[1])
    buyers.append(lst[2])

for _ in range(4):
    lst = input().split()
    bounce_rate.append(lst[1])

lowest_bounce_rate = 1000000
index = 0

for i in range(4):
    if bounce_rate[i] / buyers[i] < lowest_bounce_rate:
        lowest_bounce_rate = bounce_rate[i] / buyers[i]
        index = i

print(card_list[index])
