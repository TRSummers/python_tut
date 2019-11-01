 import math
import random
from pathlib import Path

def printCat():
    print("""
                '
                '
        ^^      '
        0--------
         | | | |  
        - - - -
    """)
    print("**" * 10)
    price=750000000000000
    print(price)

def ex1():
    print("Exercise 1")
    name=input("Name: ")
    color = input("Yo " + name + " Fave color? ")
    print("Yo, " + name + " Yeah, " + name + " I like " + color + " too")
    print(name[0:-1])

def ex2():
    print("Ex 2")
    weight=input("Wassyer weight? ")
    weight_in_klingon=int(weight)*3.124
    print(f'Weight is: {weight}. Weight in Klingon is: {weight_in_klingon}')

def strings():
    foo=name[3:-2]
    print("Foo is: " + foo)
    #String manipulation
    foo=input("Enter Text: ")
    print(foo.find("fuck"))
    smoot=(foo.replace('fuck', 'fuck the HELL OUT OF YOU'))
    print(smoot)
    print(f"smoot is {smoot}")
    len(foo)
    smarp=foo.upper()
    print(f"smarp is {smarp}")
    hoog=foo.lower()
    print(f"hoog is {hoog}")
    flep=smoot.replace("THE HELL", "Farge Bleeg")
    print(f"flep is {flep}")
    smoot=(flep.title())
    print(f"smoot is {smoot}")
    feff="FUCK" in smoot
    print(feff)

def numericals():
    num1=input("Number: ")
    num2=input("Number 2: ")
    num3=int(num1)+int(num2)
    print(f"Adding {num1} and {num2} to get {num3}")
    num3=int(num1)-int(num2)
    print(f"Subtracting {num1} and {num2} to get {num3}")
    num3=int(num1)*int(num2)
    print(f"Multiplying {num1} and {num2} to get {num3}")
    num3=int(num1)/int(num2)
    print(f"Dividing(with decimals) {num1} and {num2} to get {num3}")
    num3=int(num1)//int(num2)
    print(f"Dividing(without decimals) {num1} and {num2} to get {num3}")
    num3=int(num1)%int(num2)
    print(f"Modulo {num1} and {num2} to get {num3}")
    num3=int(num1)**int(num2)
    print(f"Exponent {num1} and {num2} to get {num3}")
    #add 'int' to the below
    fpn=input("Enter a floating point number: ")
    fpn2=float(fpn)+int(num1)
    print(f"fpn2: {fpn2} ")
    fpn3=round(fpn2)
    print(fpn)
    neg=input("enter a neg num: ")
    neg2=int(neg)
    print(abs(neg2))
    print(f"ciel of fpn2 is {math.ceil(fpn2)}")
    print(f"floor of fpn2 is {math.floor(fpn2)}")


def logic_stuff():
   temp=input("Temp: ")
   foo=int(temp)

   if foo>90:
       print("Phew! I hate this weather!")
   elif foo<90 and foo>80:
       print("At least I can sleep tonight.")
   else:
       print("Ahhhhhh!")


def house_buyer():
    house_cost=int(input("House Cost: "))
    print(house_cost)
    credit_score = input("Does the buyer have good credit?: ")
    high_income = input("Make enough money?: ")

    if credit_score=="Y" and high_income=="Y":
        dp=house_cost*0.01
        print(f"Down Payment is: {dp}")
    elif (credit_score=="Y" and high_income=="N") or (credit_score=="N" and high_income=="Y"):
        if credit_score=="Y":
            dp = house_cost * 0.4
            print(f"Don't make enuff. DP is 40% {dp}")
        else:
            dp = house_cost * 0.5
            print(f"Bad credit! DP is 50%! {dp}")
    else:
        dp=house_cost*0.7
        print(f"Too bad. Down payment is 70% {dp}")


def enter_name():
    length=int(1)
    while length<3 or length>50:
        first_name=input("Enter Your First Name: ")
        last_name=input("Enter Your Last Name: ")

        length=len(first_name)+len(last_name)

        if length<4:
            print("Too short. Enter again.")
        elif length>50:
            print("Too long. Try again.")
        else:
            print(f"your name is {first_name} {last_name}")


def weights():
    weight = float(input("Enter weight: "))
    unit = input("Lbs or Kg: ")
    print(f"unit is: {unit}")

    if unit.upper() == "L":
        converted = weight*0.45
        print(f"Weight in kilos is: {converted}")
    else:
        converted = weight/0.45
        print(f"Weight in pounds is: {converted}")

def car():
    command = ""
    started = 0
    going = 0
    go = 0
    stopped = 0
    starting = 0

    def printlines():
        print("")
        print("")

    def start(started):
        if started == 1:
            printlines()
            print("Car's already started. Let's go!!!!!!")
            printlines()
            return started
        else:
            printlines()
            print("Vroom, vroom! Ready to go!!!!")
            printlines()
            started = 1
        return started

    def drive(started, go, stopped):
        if started != 1:
            printlines()
            print("Ya gotta start the car first!")
            printlines()
        elif started == 1 and go == 2 and stopped == 0:
            printlines()
            print("You're already on your way!")
            printlines()
            go = 2
            return go
        elif stopped == 1:
            print("You're already stopped. You might want to go again.")
        else:
            printlines()
            print("Off to the autobahn! WHEEEEEE!")
            printlines()
            go = 2
            return go
        print(f"started = {started}, go={go}, stopped={stopped}")

    def brake(stopped):
        if started != 1:
            printlines()
            print("Start the car first! Y'aint goin' nowhere!")
            printlines()

        elif go != 2:
            printlines()
            print("Car's not moving!")
            printlines()

        elif stopped == 1:
            printlines()
            print("Already stopped, dummy!")
            printlines()

        else:
            printlines()
            print("SCREEEEEEEEECH!!!!! Braking! Get outta the way!!!!")
            printlines()
            print(f"stopped = {stopped}")
            stopped = 1
            return stopped

    def quit():
        printlines()
        print("Gone, Girl")
        printlines()


    while True:

        if starting == 0:
            print("""
                 Enter one of the following commands: 
                 start = 'Start'
                 drive = 'Drive'
                 stop  = 'Brake'
                 quit  = 'Quit'
                 help  = 'Help'
            =============================================
            """)
            starting = 1


        command = input("Enter command: ").upper()

        if command == "H" or command == "HELP":
          print("""
               Enter one of the following commands: 
                   start = 'Start'
                   drive = 'Drive'
                   stop  = 'Brake'
                   quit  = 'Quit'
                   help  = 'Help'
               =============================================
           """)

        elif command == "START" or command == "S":
            started = start(started)

        elif command == "DRIVE" or command == "D":
            go = drive(started, go, stopped)

        elif command == "BRAKE" or command == "B":
            stopped=brake(stopped)

        elif command == "QUIT" or command == "Q":
            quit()
            break

        else:
            print("""
            Please enter S, D, B or Q. 
            """)


def lists():

    for smid in range(42):
        print(smid)
        for smid in range(22, 42, 13):
            print(smid)
#            input("Hit Enter: ")

    for smid in ["glick", "fremd", "hoodja", "Sheelah"]:
        print(smid)

#lists()

def prices():

    prices = [10, 20, 30, 119.13, 182.66]

    total=0

    for price in prices:
        total += price
        print(f"New Item cost = {price}")
        print(f"Total = {total}")



def fu():
    exes = [10, 4, 10, 4, 4]

    def fu1():
        for ex in exes:
            lines = 0
            while lines < 2:
             print("x" * ex)
             lines += 1

    def fu2():

        for ex in exes:
            output = ''
            lines = 0
            why = 0

            #while lines < 2:
            for why in range(ex):
             print(f"{why}")
             output += 'Y'
             print(f"{output}")
             #lines += 1
    def fu3():
        exes = [13, 22, 67, 89]
        x, y, z, a = exes
        print(f"{x}, {y}, {z}, {a}")

    fu3()

def kvp_dict():

    dick={
        "Floo": "",
        "Flig": "",
        "Sexy": "",
        "Now": ""
    }

    dick["Flig"] = input("Enter your name: ")
    dick["Floo"] = input("Enter your number: ")
    dick["Sexy"] = input("Are you hot?: ")
    dick["Now"] = input("You want some dick now?: ")
    dick["Torb"] = input("Top or bottom?: ")

    a = dick["Flig"]
    b = dick["Sexy"]
    c = dick["Floo"]
    d = dick["Now"]
    e = dick["Torb"]

    print(f"{a} is sexy? {b}! His number is {c}. You want it now? {d} And he's a {e}")

    msg = input("Enter something more than one word: ")
    words = msg.split()

    print(words[2])

#kvp_dict()

def shopping_cart1():

   total_items = 1
   items = 1
   first_item = True
   price = 0
   total_price = 0
   final_price = 0
   total_discount = 0
   cont = ""
   items_to_add = 0

   def cart(price, total_items, total_price):
       total_price = price + total_price
       return total_price


   def discount(final_price):
       final_price *= .90
       total_discount = final_price * .1
       return final_price, total_discount


   def add_items(item, cost):
       print(f"adding item {items}")
       print(f"Cost is {cost}")


   while total_items <= items:
       if first_item == True:
        items = int(input("Enter number of items: "))
        first_item = False
       else:
        price = float(input(f"Enter Price for item {total_items}: "))
        print(f"Item {total_items} is ${price}")
        final_price = cart(price, total_items, final_price)
        print("")
        print(f"Total so far is: {final_price}")
        print("")
        total_items += 1

        if total_items > items:
           if final_price >= 100:
                disc, total_discount = discount(final_price)
                print(f"You have a discount! We will deduct 10% of your total, which is {total_discount}")
                print(f"Your final total will be {disc}")
           else:
                cont = input(f"Sorry, you are not eligible for a discount at this time. Would you like to continue shopping (Y or N)?: ").upper()
                if cont == "Y":
                    item = 1
                    items_to_add = int(input("Number of items you'd like to add: "))
                    while items_to_add >= item:
                        price = float(input(f"Price for item {item}: "))
                        total_price = cart(price, total_items, total_price)
                        item += 1
                        final_price += total_price
                        print(f"total price = {total_price}")
                        print(f"final price = {final_price}")

                else:
                    print(f"Sorry, no discount. Your total will be {final_price}")

#shopping_cart1()

def shopping_cart():

   total_items = 0
   items = 1
   first_item = True
   price = 0
   total_price = 0
   final_price = 0
   total_discount = 0
   cont = ""
   items_to_add = 0
   first = 0

   def cart(price, total_price):
       total_price = price + total_price
       return total_price


   def discount(final_price):
       total_discount = final_price * .1
       final_price -= total_discount
       return final_price, total_discount


   def add_items(first, final_price):
        total_items = 1
        items = 1
        final_price = 0
        total_price = 0

        while total_items <= items:
            if first == 0:
                items = int(input("Enter number of items: "))
                first = 1
            else:
                price = float(input(f"Enter Price for item {total_items}: "))
                print(f"Item {total_items} is ${price}")
                final_price = cart(price, final_price)
                print("")
                print(f"Total so far is: {final_price}")
                print("")
                total_items += 1
                #return final_price

        if total_items > items:
           if final_price >= 100:
                disc, total_discount = discount(final_price)
                print(f"You have a discount! We will deduct 10% of your total, which is {total_discount}")
                print(f"Your final total will be {disc}")
           else:
                cont = input(f"Sorry, you are not eligible for a discount at this time. Would you like to continue shopping (Y or N)?: ").upper()
                if cont == "Y":
                    item = 1
                    items_to_add = int(input("Number of items you'd like to add: "))
                    while items_to_add >= item:
                        first = 1
                        final_price = add_items(first, final_price)
                        item += 1
                        #final_price += total_price
                        print("FOO")
                        print(f"total price = {total_price}")
                        print(f"final price = {final_price}")
                        print("FOO")
                else:
                    print(f"Sorry, no discount. Your total will be {final_price}")

   add_items(first, final_price)

#shopping_cart()

def paths():
    path = Path()
    for file in path.glob('*.*'):
        print(f"{file}")


paths()

def dice():

    dudes = ["Floo", "Fligg", "Smid", "Kregg"]
    for a in range(3):
        for i in range(3):
            print(random.randint(1, 89))
            alpha = random.choice(dudes)
            print(alpha)

#dice()

class Dice:

    def roll(a, b):
        print(f"num1= {a}")
        #print(f"num2= {num2}")
        first = random.randint({a}, 100)
        second = random.randint({a}, 100)
        return first, second

    def unroll(self):
        ufirst = random.randint(1, 100)
        usecond = random.randint(100, 1000)
        return ufirst, usecond


def piff():

    dice = Dice()
#    i = 1
    num = int(input("How many rolls?: "))
    print(f"num = {num}")
    range1 = int(input("Starting range: "))
    range2 = int(input("Ending range: "))


    for iterations in range(num):

        iterations += 1
        roller = dice.roll(range1)
        print(f"Roll {iterations} is {roller}")
        unroll = dice.unroll()
        print(f"Unroll {iterations} is {unroll}")


#piff()


def fib():

    a = 0
    b = 1
    result = 0
    stop = 0

    foo = int(input("Enter a max limit: "))

    for i in range(foo):
        print(f'{result}')
        result = a + b
        b = a
        a = result

#fib()

def collatz():

    figure = 0
    limit = int(input("enter max number: "))
    yorn = input("Figure all the numbers below?: ")

    original = limit

    for figure in range(original):

        while (limit > 1):

                if ( limit % 2 == 0 ):
                    limit = limit/2
                else:
                    limit = limit*3+1

                figure += 1
                if (limit == 1):
                    print(f"Original Number = {original} Number of steps = {figure} final number is {limit}")


collatz()

   \
