# -*- coding: utf-8 -*-
row=int(input("Enter rows:"))
for i in range(row):
    for j in range(i,row):
     print("*",end=" ")
    for j in range(i):
          print("*",end=" ")
    for j in range(i+1):
           print("* " ,end=" ")
    print()
    