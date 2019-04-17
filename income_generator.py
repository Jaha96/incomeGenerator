from random import randint
import json
from pprint import pprint

currentYear = 2019
currentMont = 2
daysOfMonth = 22
monthlyNormalIncome = 4500000

firstDailyNormalIncome = (monthlyNormalIncome/daysOfMonth)

print("days of month is: " + str(daysOfMonth))
print("monthy normal income is: " + str(monthlyNormalIncome))


# import product list from json file
jsonFile = open('income_data.json', encoding='utf-8')
jsondata = json.load(jsonFile)
products = jsondata["products"]
productLength = len(products)

f= open("income_file.txt","w+", encoding='utf-8')

for day in range(1, daysOfMonth+1):
    dailyIncome = 0.0
    dailyNormalIncome = (monthlyNormalIncome/(daysOfMonth-(day-1)))
    downPercent = (dailyNormalIncome*100.0)/firstDailyNormalIncome
    if downPercent < 31.0:
        dailyNormalIncome = firstDailyNormalIncome
    print("daily normal income is: " + str(dailyNormalIncome))
    while dailyIncome < dailyNormalIncome:
        randomProduct = products[randint(0, productLength-1)]
        ashig = (randint(29,35)*0.01)
        print("ashig huwi: " + str(ashig))
        q = int(randomProduct["maxDailyQuantity"])
        quantity = randint(1,q)
        name = randomProduct["name"]
        price = float(randomProduct["price"])
        totalPrice = quantity*price
        vat = float(totalPrice)*0.1
        income = (totalPrice-vat)
        income *= ashig
        f.write(str(name) + "\t" + str(quantity) + "\t" + str(price) + "\t" + str(totalPrice) + "\t" + str(vat) + "\t" + str(income) + "\t" + str(currentYear) + "." + str(currentMont) + "." + str(day) + "\n")
        dailyIncome +=income
        monthlyNormalIncome -= income
    print("day is: " + str(day))
f.close() 

print("------------ Script finished ----------------")

