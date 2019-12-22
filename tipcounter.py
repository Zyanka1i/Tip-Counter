#TIPCOUNTER 1.0

# Eingabe vom tatsächlichen Preis
price = float(input("Geben sie den Preis ein: "))
# Barzahlung
cash = float(input("Geben sie die Bahrzahlung ein: "))

#Die gegebene Summe inkl. Trinkgeld
given = float(input("Geben Sie vom Kunden gennante Summe ein: "))

#Trinkgeld
tip: float = (given - price)

#Wechselgeld
change: float = (cash - price - tip)

# Calkuliert den Unterschied der beiden Summen, wenn die Barzahlung grösser ist als der Preis
def changecalculator ():
	pass 
if given >= price:
    print("Ihr Wechselgeld ist: ", change)
else:
    print(change)
#Ausgabe Trinkgeld
print("Tip: ", tip)

Total: float = (0 + tip)
print("Total Tip: ", Total)