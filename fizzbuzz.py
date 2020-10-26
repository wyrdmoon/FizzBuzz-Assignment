def number(list):
  for number in list:  
    if (number % 3 == 0 and number% 5 == 0):
      print("FizzBuzz")
    elif (number % 3 == 0):
      print("Fizz")
    elif (number % 5 == 0):
      print("Buzz")
    else:
      print(number)


list = [45,22,18,23,50,21,10,3,99,55,34,44,71,30,9,33,71,87,31,20]
number(list)

    