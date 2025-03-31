num=int(input("Please enter a number"))
res=0
temp=num

while temp!=0:
    digit=temp%10
    res=res+digit**3
    temp=temp//10
print(res)

if num==res:
    print("it is an armstrong number")
else:
    print("it is not a armstrong number")

#factorisation 
num=int(input("Please enter a number"))
print(f"All the factors of{num} are")
for i in range(1,num+1):
    if (num%i==0) :
        print(i)


#roman 2 int

def roman2int(a):
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    intform=0
    for i in range(len(a)):
        if i+1<len(a) and roman[a[i]]<roman[a[i+1]]:
            intform-=roman[a[i]]
        else:
            intform+=roman[a[i]]
    return intform

a=(input("please enter a roman number"))
print("corresponding integer no. is ",roman2int(a))