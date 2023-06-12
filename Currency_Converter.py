# I Acquired this Data from https://www.x-rates.com/table/?from=INR&amount=1

f = open("currency.txt")
lines = f.readlines()

currency_dict = {}
for line in lines :
    parsed = line.split("\t")
    # Filling the empty currency_dict dictionary by parsing the lines

    currency_dict[parsed[0]] = parsed[1]

amount = int(input("Enter Your desired amount which you want to covert : \n"))

for items in currency_dict.keys() :
    print(items)
currency = input("Enter one of these currency you want to convert your amount to : \n")

print(f"{amount} INR is {amount * float(currency_dict[currency])} {currency}")
