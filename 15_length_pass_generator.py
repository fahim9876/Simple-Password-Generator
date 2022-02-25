#made by fahim
#I am new in python
import random
lower = "abcdufghijklmnopqrstuvwxyz"
upper = "ABCDUFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "{}[]()#;.,+-*$@"
print("PLease enter your password length")
x = int(input())
all = lower + upper + number + symbol
length = x
password = "".join(random.sample(all,length))
print("Your password is",password)







