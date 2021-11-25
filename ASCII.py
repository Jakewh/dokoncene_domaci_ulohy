# ASCII tabulka

print("ASCII tabulka\n=============")
cisla = list(range(0,256))
for i in cisla:
    print(i, ":", chr(i), "\t", end="")
input()
