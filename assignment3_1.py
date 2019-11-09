'''Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130'''
from functools import *
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
    #using sum method
    #result = sum(RawData)
    #result = reduce(RawData)
    result =reduce(lambda no1,no2:no1+no2,RawData)
    
    print("output=",result)
    
if __name__ == "__main__":
    main() 