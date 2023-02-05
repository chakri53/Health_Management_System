import datetime


def gettime():
    return datetime.datetime.now()


def inputt(n):
    if n == 1:
        d = int(input("Enter 1 for excerise and 2 for food :"))
        if d == 1:
            value = input("type here.. \n")
            with open("chakri-exe.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n ")
            print("written successfully ")
        elif d == 2:
            value = input("type here.. \n")
            with open("chakri-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n ")
            print("written successfully ")
    elif n == 2:
        d = int(input("Enter 1 for exercise and 2 for food :"))
        if d == 1:
            value = input("type here.. \n")
            with open("viswa-exe.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n ")
            print("written successfully ")
        elif d == 2:
            value = input("type here.. \n")
            with open("viswa-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n ")
            print("written successfully ")
    elif n == 3:
        d = int(input("Enter 1 for exercise and 2 for food :"))
        if d == 1:
            value = input("type here.. \n")
            with open("muni-exe.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n ")
            print("written successfully ")
        elif d == 2:
            value = input("type here.. \n")
            with open("muni-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n ")
            print("written successfully ")
    else:
        print("Enter the valid input 1(chakri) 2(viswa) 3(muni)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("chakri-exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("chakri-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("viswa-exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("viswa-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 3:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("muni-exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("muni-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (chakri,viswa,muni)")


print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for chakri 2 for viswa 3 for muni "))
    inputt(b)
else:
    b = int(input("Press 1 for chakri 2 for viswa 3 for muni "))
    retrieve(b)