#for (x) in range(10):
    #print("hello world.")
#import sys

#print(sys.version)
#print(sys.copyright)




"""
if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!") 
if 5 > 2:
     print("Five is greater than two!")
"""

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

list = [x, y, z]
print(list)
print(*list)

x = 5
y = "John"
print(x, y)

x = "awesome"

def myfunc():
  #global x 
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

txt = "The best things in life are free!"
print("free" in txt)

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello"
b = "World"
c = a + b
print(a,b)