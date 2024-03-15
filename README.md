# Python-Week--1
Python is case sensitive so it is important that you use the correct case, otherwise your code will not work.

Text values need to appear in speech marks (") but numbers do not. When naming variables (i.e. values that you want to store data in) you cannot use any dedicated words such as print, input, etc. otherwise your code will not work.

If statements allow your program to make a decision and change the route that is taken through the program

Indenting is very important in Python as it shows the lines that are dependent on others, as shown in the example on the previous page. In order to indent text you can use your [Tab] key or you can press your [space key] five times. The [backspace] key will remove indents.  

String is the technical name for text. To define a block of code as a string, you need to include it in either double quotes (") or single quotes ('). It doesn’t matter which you use so long as you are consistent. 

len(word) Finds the length of variable called word. 

print(word.capitalize()) Displays the variable so only the first word has a capital letter at the beginning and everything else is in lower case. 

word.upper() Changes the string into upper case. 
word.lower() Changes the string into lower case
word.title() Changes a phrase so that every word has a capital letter at the beginning with the rest of the letters in the word in lower case (i.e.Title Case)
text = “ This is some text. ” print(text.strip(“ ”)) Removes extra characters (in this case spaces) from the start and end of a string. 

print(round(num,2)) Displays a number rounded to two decimal places.

math.sqrt(num) The square root of a number, but you must have the line import math at the top of your program for this to work

A for loop allows Python to keep repeating code a set number of times. It is sometimes known as a counting loop because you know the number of times the loop will run before it start

for i in range(1,10):  print(i)

for i in range(1,10,2):  print(i) This range function includes a third value which shows how much is added to i in each loop (in this case 2). The output will therefore be: 1, 3, 5, 7, 9 

for i in range(10,1,-3):  print(i) This range will subtract 3 from i each time. The output will be: 10, 7, 4 

enclose your text within triple quotes

A while loop allows code to be repeated an unknown number of times as long as a condition is being met. This may be 100 times, just the once or even never. In a while loop the condition is checked before the code is run, which means it could skip the loop altogether if the condition is not being met to start with. It is important, therefore, to make sure the correct conditions are in place to run the loop before it starts.  
![alt text](image.png)

Python can generate random values. In reality, the values are not completely random as no computer can cope with that; instead it uses an incredibly complex algorithm that makes it virtually impossible to accurately predict its outcome so, in effect, it acts like a random function. 
There are two types of random value that we will be looking at: 
 Random numbers within a specified range; 
 A random choice from a range of items that are input. To use these two options, you will need to import the random library. You do this by typing import random at the start of your program.  

Once a tuple is defined you cannot change what is stored in it. This means that when you write the program you must state what the data is that is being stored in the tuple and the data cannot be altered while the program is running. Tuples are usually used for menu items that would not need to be changed

The contents of a list can be changed while the program is running and lists are one of the most common ways to store a collection of data under one variable name in Python. The data in a list does not all have to be of the same data type. For example, the same list can store both strings and integers; however, this can cause problems later and is therefore not recommended. 

Dictionaries  The contents of a dictionary can also be changed while the program is running. Each value is given an index or key you can define to help identify each piece of data. This index will not change if other rows of data are added or deleted, unlike lists where the position of the items can change and therefore their index number will also change.