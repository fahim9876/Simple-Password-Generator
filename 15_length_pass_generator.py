#made by fahim
#I am new in python
import random
lower = "abcdufghijklmnopqrstuvwxyz"
upper = "ABCDUFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "{}[]()#;.,+-*$@"
print("Your password is below....")
x = int(input())
all = lower + upper + number + symbol
length = x
password = "".join(random.sample(all,length))
print(password)







