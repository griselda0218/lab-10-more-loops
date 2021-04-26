string = input("gimme a number that is greater than 100")
num = int(string)
while (num < 100 ): #test condition when termination is not true
    print(str(num) + " is less than 100, try again..")
    string = input("gimme a number that is greater than 100")
    num = int(string)
print(str(num) + " is greater than 100! finally!")
