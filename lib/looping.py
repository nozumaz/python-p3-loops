#!/usr/bin/env python3


def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    for i in range(len(int_list)):
        int_list[i] *= int_list[i]
    return int_list

def fizzbuzz():
    # code goes here!
    i = 0
    while i < 100:
        i += 1
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
    pass
