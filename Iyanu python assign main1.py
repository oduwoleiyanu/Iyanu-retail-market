# import json

class RetailMarket:
    """ Mr Adamu's Shop """

    def __init__(self):
        self.items = []
        self.gain = 0
        items = [{"name": "Sugar", "quantity": 131, "price": 50}, {"name": "Bread (sliced)", "quantity": 311, "price": 200}, {"name": "Bread (unsliced)", "quantity": 229, "price": 150}, {
            "name": "Egg", "quantity": 545, "price": 50}, {"name": "Three crown (tin)", "quantity": 201, "price": 150},{"name": "Peak milk (tin)", "quantity": 230, "price": 120},{"name": "Peak milk (sachet)", "quantity": 791, "price": 50},{"name": "Bournvita(sachet)", "quantity": 611, "price": 50},{"name": "Milo (tin)", "quantity": 367, "price": 500},{"name": "Peak milk (large sachet)", "quantity": 889, "price": 700}]

        for obj in items:
            item = Item(obj['name'], obj['quantity'], obj['price'])
            self.items.append(item)

    def addItem(self, name, quantity, price):
        item = Item(name, quantity, price)
        self.items.append(item)

    def getItem(self, name):
        item = next((item for item in self.items if item.name == name), None)
        return item

    def purchaseGoods(self, name, items):
        customer = Customer(name)
        customer.name = name
        price = 0
        priceLeast = 0

        for item in items:
            price += int(item.price) * int(item.quantity)
            realItem = self.getItem(item.name)
            realItem.updateStock(item.quantity)
            if item.price >= 100:
                priceLeast = 1

        customer.computeTotalPrice(price)

        # take record of gain
        self.computeGain(price)

        if len(items) < 5:
            customer.addVAT(20)
        else:
            customer.addVAT(30)

        if len(items) > 5 and priceLeast == 1:
            customer.bonusGoodsAmount = 800

        print("\nPlease print your receipt\n\n")
        print("\nName: {}\n".format(customer.name))
        print("\nTotal Price: {}\n".format(customer.totalPrice))
        print("\n{}% VAT: {}\n".format(customer.percentVAT, customer.VAT))
        print("\nTotal Price with {}% VAT: {}\n".format(
            customer.percentVAT, customer.totalPriceVATInc))
        print("\nBonus Goods Amount: {}\n".format(customer.bonusGoodsAmount))
        print("{:<8} {:<25} {:<10} {:<10}".format(
            'S/No', 'Item', 'Qty bought', 'Price'))
        for item in items:
            print("{:<8} {:<25} {:<10} {:<10}".format(
                items.index(item) + 1, item.name, item.quantity, item.price))

    def computeGain(self, price):
        self.gain = int(self.gain) + int(price)

    def viewGain(self):
        print("\nYour total gain today is: {}\n".format(self.gain))

    def displayItems(self):
        print("\n{:<8} {:<25} {:<10} {:<10}".format(
            'S/No', 'Item', 'Av Qty', 'Price'))
        for item in self.items:
            print("\n{:<8} {:<25} {:<10} {:<10}".format(
                self.items.index(item) + 1, item.name, item.quantity, item.price))


class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = int(quantity)
        self.price = int(price)

    def changePrice(self, newPrice):
        self.price = int(newPrice)

    def updateStock(self, quantity):
        self.quantity = int(self.quantity) - int(quantity)


class Customer:
    def __init__(self, name):
        self.name = name
        self.totalPrice = 0
        self.totalPriceVATInc = 0
        self.percentVAT = 0
        self.VAT = 0
        self.bonusGoodsAmount = 0

    def computeTotalPrice(self, totalPrice):
        self.totalPrice = totalPrice

    def addVAT(self, percent):
        self.percentVAT = percent
        vat = int(self.totalPrice) * (int(percent)/100)
        self.VAT = vat
        self.totalPriceVATInc = int(self.totalPrice) + int(vat)

    def bonusGoods(self, amount):
        self.bonusGoodsAmount = int(amount)
