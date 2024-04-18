
#Exercise 1
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp"+
      " above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle,"+
      " twinkle, little star,\n\tHow I wonder what you are.")
#Exercise 2
x = input("Inter your number :")
try:
    val = int(x)
    if val % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
except ValueError:
    print("That's not an int!")
    
#Exercise 3
x = input("Inter your number 1 :")
y = input("Inter your number 2 :")
try:
    val1 = int(x)
    val2 = int(y)
    if val1 * val2 <= 1000:
        print("The result is", val1 * val2)
    else:
        print("The result is", val1 + val2)
except ValueError:
    print("That's not an int!")
    
#Exercise 4
x = input("Input a numer between 100-999 :")
try:
    val1 = int(x)
    if val1 <100 or val1 > 999:
        raise IndexError("Number is out of range!")
    y = x[::-1]
    print(f"The reverse is {y}.")
except ValueError:
    print("That's not an int!")
except IndexError as indexerror:
    print(indexerror.args)