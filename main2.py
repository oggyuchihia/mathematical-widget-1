from math import sqrt

num=int(input("Enter the number: "))
if num>1:
    for i in range(2,int(sqrt(num))+1):
        if num%i==0:
            print("no. is not prime")
            break
    else:
        print("no. is prime")
else:
    print("no. is not prime")

#sieve off eraspothinise
def sieve(n):
    prime=[True for i in range(n+1)]
    curnum=2
    while(curnum*curnum<=n):
        if(prime[curnum]==True) :
            for i in range(curnum**2,n+1,curnum):
                prime[i]=False
        curnum+=1
    prime[0]=False
    prime[1]=False
    for i in range(n+1):
        if prime[i]:
            print(i)

n=int(input("enter a num within which you want to find prime no.s"))
sieve(n)
