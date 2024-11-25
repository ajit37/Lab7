#!/usr/bin/env python3
# Student ID: avirk18

def function1():
    global schoolName # Using global variable
    schoolName = 'SICT'  # This creates a local variable 'schoolName'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName # global variable
    global schoolName  # This modifies the global 'schoolName'
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)
function2()
print('print() in main on schoolName:', schoolName)
