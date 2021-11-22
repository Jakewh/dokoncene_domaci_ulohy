print("Tento prográmek ti řekne, zda tvoje slovo je palindrom.")
pokracovat = True
while pokracovat:
    slovo = input("Zadej slovo: ")
    slovo_pozpatku = slovo[::-1]
    if slovo == slovo_pozpatku:
        print("Tohle slovo je palidrom.")
    else:
        print("Tohle slovo není palindrom.")
    znovu = input("Pokračovat? ano/ne: ")
    if znovu == "ano":
        continue
    else:
        break
input("Stiskem klávesy ukončíš program")
