data = []
print("Enter numbers. To end the entry, press the ENTER key")
while True:
	number = input("Enter number: ")
	if number == "":
		break
	data.append(int(number))
data_2 = sorted(data)
median = data_2[len(data_2)//2]
for i in data_2:
	print(i, " differs from the median by: ", i - median)
input()
