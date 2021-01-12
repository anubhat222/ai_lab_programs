#print hello world
print("Hello World!")

#to add 2 numbers
a,b=2,3
print(a+b)

#to find the squareroot
import math
a=25
print(math.sqrt(a))

#to find area of the triangle
a,b,c=map(int,input("Enter sides of triangle:").split())
s = (a + b + c) / 2
print(float((s*(s-a)*(s-b)*(s-c))**0.5))

#to find roots of the quadratic equation
import cmath
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)

print("The Solution are:",sol1,"and",sol2)

#swapping 2 nos
a,b=map(int,input("Enter a and b").split())
print("The value of a is",a,"The value of b is ",b,"before swapping")
a=a-b
b=a+b
a=b-a
print("The value of a is",a,"The value of b is ",b,"after swapping")

#random integer
import random
r=random.randint(1,6)
print(r)

#km to miles
km=float(input("Enter the kilometers:"))
m=0.612*km
print("The miles are :",m,"miles")

#degree to celsius
c=float(input("Enter the temperatures in degree celsius"))
f=(c*9/5)+32
print("the value of ", c, "in farenheit is:",f)

#sorting a list in ascending and descending order
l=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    ele = int(input()) 
    l.append(ele)
l.sort()
print("the list in ascending order:",l)
l.sort(reverse=True)
print("The list in descending order:",l)

    















