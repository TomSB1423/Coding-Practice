# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = int(input())
sizes = Counter(list(map(float, input().split(" "))))
N = int(input())
money = []
for i in range(N):
    customer = list(map(float, input().split(" ")))  # Shoe size, price
    if customer[0] in sizes:
        if sizes[customer[0]] >= 1:
            sizes[customer[0]] = sizes[customer[0]] - 1
            money.append(customer[1])
print(int(sum(money)))
