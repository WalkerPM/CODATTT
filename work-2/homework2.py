#!/usr/bin/python3

number = int(input("Write a number greater 1000 and lower 10000\n"))
out = int(0)

if number < 1000 or number > 9999:
	print("Invalid number!")
	exit()
else:
	out += (number % 10) + (number // 1000)
	out += ((number % 100) // 10) + ((number % 1000) // 100)
	print(out)

print("Done")
