import math
import statistics
import pandas


#the X&Y axis 
x = []
y = []

#This is the Dracula book and the process of opening and reading it. 
#then afterwards splitting the book up prod by people
file = open("feedbooks_book_88", "r")
data = file.read()
clean_data = data.split(".")

#this code is to create the data point for the graph
for i in range(len(clean_data)):
  x.append(i)
y = [sum(x == "dracula".lower() for x in i) for i in clean_data]


