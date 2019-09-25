#/usr/bin/python3

obj = [0,0,""]

print("This is a calculator, please follow instruction.")

obj[0] = int(input("Write a first number: ")) # Yeah, i'm remind youself about ")"
obj[1] = int(input("Write a second number: "))
obj[2] = str(input('Write a math operator ( "/" - divide, "*" - multiply, "+" - plus, "-" - minus ) '))

try:				#Seriously, python haven't switch-case construction?77??
	if obj[2] == "/":
		out = obj[0] / obj[1]
	elif obj[2] == "*":
		out = obj[0] * obj[1]
	elif obj[2] == "+":
                out = obj[0] + obj[1]
	elif obj[2] == "-":
                out = obj[0] * obj[1]
	else:
		print("Undefined operator")
		exit()
	print(out)

except ZeroDivisionError:
	print("Please, don't try to divide by zero, it scares PC")

print("Done")

