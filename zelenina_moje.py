zelenina = ["rajče", "mrkev", "okurka"]
ovoce = ["banán", "pomeranč", "citron"]
pocet_dotazu = 0
opakovat = True
while opakovat:
        nazev = input("Zadej název zeleniny nebo ovoce: ")
        if nazev in zelenina:
                print("Napsal jsi zeleninu.")
        elif nazev in ovoce:
                print("Napsal jsi ovoce.")
        else:
                print("Tohle nemám v seznamu.")
        pocet_dotazu += 1
        znovu = input("Chceš zadat další slovo? ano/ne: ")
        if znovu == "ano":
                continue
        else:
                break
print("Celkem napsáno dotazů: ", pocet_dotazu)
input()
