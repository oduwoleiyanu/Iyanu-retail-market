##C:/Users/Lyanu/AppData/Local/Temp/Rar$DRa14072.31587/Python Assignment/main.py
from main import RetailMarket
from main import Item


class Test:
    def __init__(self):
        pass

    def addItem(self):
        name = input("\nEnter Item name\n")
        quantity = input("\nEnter Item quantity\n")
        price = input("\nEnter Item price\n")
        stock.addItem(name, quantity, price)
        stock.displayItems()

    def viewGain(self):
        stock.viewGain()

    def changePrice(self):
        name = input("\nEnter Item name\n")
        item = stock.getItem(name)
        if item != None:
            price = input("\nEnter Item new price\n")
            item.changePrice(price)
            stock.displayItems()
        else:
            print("\nItem not found")

    def purchaseGoods(self):
        stock.displayItems()
        customerName = input(
            "Enter your name\n")
        items = []
        name = input(
            "Enter the name of the products you want to buy. Enter -1 to end\n")
        while name != "-1":
            realItem = stock.getItem(name)
            if realItem != None:
                quantity = input("\nEnter quantity\n")
                item = Item(realItem.name, quantity, realItem.price)
                items.append(item)
            else:
                print("\nItem not found")
            name = input("\nEnter another product. Enter -1 to end\n")

        stock.purchaseGoods(customerName, items)


def start():
    k = input("\nWhat do you want to do?\n\nEnter a number to do something\n1. View available items\n2. Add an item to stock\n3. Change price of an item\n4. Purchase goods\n5. View total gain today\n-1. Exit the system\n\n")
    if k != "-1":
        if k == "1":
            stock.displayItems()
            start()
        elif k == "2":
            test.addItem()
            start()
        elif k == "3":
            test.changePrice()
            start()
        elif k == "4":
            test.purchaseGoods()
            start()
        elif k == "5":
            test.viewGain()
            start()
        else:
            start()


stock = RetailMarket()
test = Test()
start()





