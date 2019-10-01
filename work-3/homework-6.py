#!/usr/bin/python3
percent = 1.03 # 3%
s = int(input("Summ of your cash? "))
n = int(input("Years for store? "))

for i in range(n):
	s = s * percent
print(s)

