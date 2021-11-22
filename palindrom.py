print("Tento prográmek ti řekne, zda tvoje slovo je palindrom.")
slovo = input("Zadej slovo: ")
slovo_pozpatku = slovo[::-1]  # neobrací slovo :(
if slovo == slovo_pozpatku:
	print("Tohle slovo je palidrom.")
else:
	print("Tohle slovo není palindrom.")
input()
