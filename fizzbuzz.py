def fizzbuzz(checkNumber):
    if checkNumber % 3 == 0:
        print("fizz")
        print(checkNumber)
    elif checkNumber % 5 == 0:
        print("buzz")
        print(checkNumber)
    elif checkNumber % 3 == 0 and checkNumber % 5 ==0:
        print ("fizzbuzz")
        print(checkNumber)
    