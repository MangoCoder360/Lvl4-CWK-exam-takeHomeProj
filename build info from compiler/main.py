# VOTE FOR JOE BIDEN! #Election2020
# I can't vote so vote for me! #JoeBiden
import easygui
class store:
    def __init__(self):
        # I tried to do it with a dictionary but couldn't remember how. Let's do it with a list/array instead!
        # inventory = {"key":"value"}   is how you make a dictionary but that is all i know.
        global inventory
        global prices
        global shopName
        global order
        inventory = ["laptop", "macBookPro", "windows10licence", "headphones"]
        prices = ["500", "3000", "100"]
        shopName = "360 Tech"
        order = []
    def greetCustomer(self, customerName):
        easygui.msgbox("Welcome to 360 Tech " + customerName + "! How can I help you today?")
    def listStock(self):
        easygui.msgbox("We have a cheap laptop, a Macbook Pro, a pair of Headphones, and a Windows10 Licence Key")
    def makeOrder(self):
        global inventory
        global order
        toAdd = easygui.buttonbox("Choose a item you would like to buy:", choices = inventory)
        order.append(toAdd)


# Using the store class

myStore = store()
myStore.greetCustomer("Joe Biden")
myStore.listStock()
myStore.makeOrder()

# I demonstrated that I understand classes and arrays/lists and I do not have time to finish the rest so this is where the program ends
