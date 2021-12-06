import string

print("Megatajný šifrovací program")

abeceda = list(string.ascii_lowercase)    # importujeme abecedu
vstup = list(input("Zadej slovo k zašifrování: "))
heslo = list(input("Zadejte šifrovací heslo: "))

while len(heslo) < len(vstup):
    heslo = heslo + heslo

