print("Program na výpočet kvadratické rovnice\nTvar rovnice: ax^2+bx+c=0")
a = int(input("Zadej koeficient a: "))
b = int(input("Zadej koeficient b: "))
c = int(input("Zadej koeficient c: "))
D = b ** 2 - 4 * a * c
if D >= 0:
	x_1 = (- b - D / D) / 2 * a
	x_2 = (- b + D / D) / 2 * a
	print("Rovnice má dva kořeny:")
	print("Kořen jedna je: ", x_1)
	print("Kořen dvě je: ", x_2)
else:
	print("Rovnice nemá řešení.")
input()
