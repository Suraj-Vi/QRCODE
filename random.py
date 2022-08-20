import random

Compno=random.randrange(1,101)
Userno=int(input("Enter your number ---:"))

if Compno<Userno:
    print("Computer number is ---:",Compno)
    print("Your number is higher than computer")

elif Compno==Userno:
    print("Computer number is ---:",Compno)
    print("Your number is equal to computer")

else:
    print("Computer number is ---:",Compno)
    print("Your number is lower than computer")