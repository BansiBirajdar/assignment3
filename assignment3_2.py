'''2.Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56'''
def Max(data):
    if len(data)==0:
        return
    max=data[0]
    for i in range(1,len(data),1):
        if max<data[i]:
            max=data[i]
    return max

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
    #using max method
    #result=max(RawData )
    result =Max(RawData)

    print("output=",result)
    
if __name__ == "__main__":
    main() 