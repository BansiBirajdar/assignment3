'''Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime().
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 54 (13 + 5 + 7 +2 + 5)'''

from functools import *
from MarvellousNum import *;

def Add(no1,no2):
    return no1+no2 

def AcceptData():
    size = int(input("Enter number of elements"))
    arr= list()
    print("Enter the elements")
    for i in range(0,size,1):
        print("Enter number",i + 1)
        no = int(input())
        arr.append(no)
    return arr



def main():
    RawData =AcceptData()
    print("Accepted data is ")
    print(RawData)
    ListPrime=list(filter(ChekPrime,RawData))
    print("ListPrime",ListPrime);
    #using sum method
    #result = sum(ListPrime)
    #result = reduce(ListPrime)
    result =reduce(lambda no1,no2:no1+no2,ListPrime)
    print("output=",result)
if __name__ == "__main__":
    main() 