# -*- coding: utf-8 -*-
"""PyLab-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19sQv-NLBApDeihcUp2I5ooKUet6cd7bb

# Cube of a Number (Without Parameters)
"""

def cube():
  n=int(input("Enter no.: "))
  print("Cube is:",n*n*n)
cube()

"""# Cube of a Number (With Parameters)"""

def cube(n):
  return(n*n*n)
a=int(input("Enter no.: "))
cub=cube(a)
print("Cube is:",cub)

"""# Area of Circle (Without Parameters)"""

def ar():
  r=float(input("Enter radius: "))
  area=3.14*r*r
  print("Area is:",area)
ar()

"""# Area of Circle (With Prameters)"""

def ar(r):
  return(3.14*r*r)
n=float(input("Enter radius: "))
area=ar(n)
print("Area is:",area)

"""# Sum from n1 to n2 (Without Parameters)"""

def s():
  n1=int(input("Enter n1: "))
  n2=int(input("Enter n2: "))
  c=0
  for i in range(n1,n2+1):
    c=c+i
  print("Sum is:",c)
s()

"""# Sum from n1 to n2 (With Parameters)"""

def s(n1,n2):
  c=0
  for i in range(n1,n2+1):
    c=c+i
  return(c)
a=int(input("Enter n1: "))
b=int(input("Enter n2: "))
sums=s(a,b)
print("Sum is:",sums)

"""# Sum from n1 to n2 (Key Arguments)"""

def s(n1,n2):
  c=0
  for i in range(n1,n2+1):
    c=c+i
  return(c) 
sums=s(n2=7,n1=2)
print("Sum is:",sums)

"""# Sum from n1 to n2 (Default Arguments)"""

def s(n1=2,n2=7):
  c=0
  for i in range(n1,n2+1):
    c=c+i
  return(c)
ans=s(3)
print("Sum is:",ans)