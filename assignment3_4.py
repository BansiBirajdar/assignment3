'''4.Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3'''
def Count(data,no):
    if len(data)==0:
        return
    else:
        icnt=0;
        for i in range(0,len(data),1):
            if data[i]==no:
                icnt+=1
        return icnt
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
    no=int(input("Element to search ="))
    print("Accepted data is ")
    print(RawData)
    #using count method
    #result=RawData.count(no)
    result=Count(RawData,no)
    print("output=",result)
    
if __name__ == "__main__":
    main() 