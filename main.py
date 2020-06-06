'''
Name: Hossain Ahmad Sobhen Morshed
Date: Nov-17-2019

Exam #2 Part #1 –  (50 points).  Post your SOURCE Python code to Moodle so I can download and run it.  Remember to implement “Good Python Programming Style” as per Python Programming rubric.  Remember to do both “positive testing” (i.e. your program produces the correct result), and “negative testing” (your program rejects negative input). Good Luck,and give me your Best Work!!

Count Lines, words, and characters in a file. (50 points): One of the most memorable speeches in US history is the “Gettysburg Address” by Abraham Lincoln. Your task is to create a Python program that will read the file (“Gettysburg_Address.txt) as input, and count the number of lines, the number of words, and the number of characters in the file.  Spaces and other whitespace do not count as characters. Files “Gettysburg_Address.txt” and “testfile.txt” are up on Moodle for your use.

'''
import numpy as np

# Question No: 1 Count line, word and charecter
# ---first method---
# loading the txt file in Python
# Loading 'testfile.txt' test file by using genfromtxt
# If i don't use delimiter while  loading the file some reason program crash
testfile = np.genfromtxt('testfile.txt', dtype=None, delimiter=",")
print(testfile)

'''
To load the text file "Gettysburg_Address.txt". i tried to load the test file by using genfrom test but because of
special charecter 'ó', it's fail to load in python. I tried hard but at the end, i decide to remove the special charecter 'ó'
by using find and replace option from notepad, and save file as a 'Gettysburgtest.txt'
by using 'open' i am able to load the test file in python, this method i find from internet line 26 to 28.
'''
with open('Gettysburgtest.txt') as Gettysburg:
    textcontent = Gettysburg.readlines()
textcontent = [x.strip() for x in textcontent]
print(textcontent)
'''
--We can also load the 'testfile' as below:--
with open('testfile.txt') as testfile1:
    textcontent_testfile = testfile1.readlines()
textcontent_testfile = [x.strip() for x in textcontent_testfile]
print(textcontent_testfile)
'''

'''
So i writer a function, wich work pretty fine, if you load your text file as a list and if each line represent one element
in a list
'''


def count(data):
    total_line = 0
    count_word = 0
    total_char = 0
    for i in data:
        # print(i)
        x = i.split()
        # print(x)
        total_line = total_line + 1
        count_word = count_word + len(x)
        total_char = total_char + len(i) - (len(x) - 1)

    return total_line, count_word, total_char


# We are calling the function using testfile as input
line, word, charecter = count(testfile)
print("----The total line word and charecter of testfile is---- ")
print("Number of line in testfile =", line)
print("Number of word in testfile =", word)
print("Number of charecter in testfile =", charecter)

'''
We are calling the function for textcontent. when we run the function it can count line and word,
we did not clean the file after loading the file so when it count charecter it did not give the correct
result. So i try to find alternate method which can work more efficiently.
'''

line, word, charecter = count(textcontent)
print("----The total line and word of Gettysburg_Address is---- ")
print("Number of line =", line)
print("Number of word =", word)
#print("Number of charecter =", charecter)

'''
So I write python code again to count charecter properly for Gettysburg text
'''
aa = []
index = 0
for j in textcontent:
    aa.append([])
    for i in j:
        i.split()
        aa[index].append(i)
    index += 1
textcontent1 = aa
# print(textcontent1)
# print(len(textcontent1))

'''
Now I write a code to delete all character like empty space ' ', comma, full stop, '"' and other charecter which i listed below
'''
remove = {' ', '"', ',', '.', "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "["}
#xa={' ', 'ó',',','.','-', '"'}
a = []
index = 0
for j in textcontent1:
    a.append([])
    for i in j:
        if i not in remove:
            a[index].append(i)
    index += 1
newtextfile = a

# print(a)
# print(len(a))
'''
I modified my frist function to count the charecter.
'''


def charecter_count(data):
    total_line = 0
    total_char = 0
    for i in data:
        total_line = total_line + 1
        total_char = total_char + len(i)
    return total_line, total_char


line1, charecter1 = charecter_count(a)
print("----The total charecter of Gettysburg_Address is---- ")
print("Number of line =", line1)
#print("Number of word =", word1)
print("Number of charecter =", charecter1)


'''
Final thought
I never work this kind of excercise before, it is a very good excercise for me.
I believe there is a better way to do this exercise, could you please provide feedback, as well as
How can i load text file in python which has invalid cherecter like we have in our text ''ó''
'''
