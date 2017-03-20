#This program prints out the number of entries in a Fibonacci series dictated by the user

#Fibonacci sequence
n=int(input('How many entries of the Fibonacci sequence would you like to be generated? '))
a,b,i=0,1,1 #assign variables, including initiating variable for while statement
print(a)
while i+1<=n:
    i=i+1
    a,b=b,a+b
    print(a)
