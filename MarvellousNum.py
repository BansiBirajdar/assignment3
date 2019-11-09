def ChekPrime(no): 
    i=0;
    for i in range(2,no+1):
        if(no%i==0):
            break
    if no==i:
        return i