'''3.Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
Input : Number of elements : 4
Input Elements : 13 5 45 7
Output :5'''
def Min(data):
    if len(data)==0:
        return
    min=data[0]
    for i in range(1,len(data),1):
        if min>data[i]:
            min=data[i]
    return min

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
    #using min method
    #result=min(RawData )
    result =Min(RawData)

    print("output=",result)
    
if __name__ == "__main__":
    main() 