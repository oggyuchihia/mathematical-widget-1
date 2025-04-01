num=int(input("enter the number"))
temp=num

revnum=0
while temp>0:
    digit=temp%10
    revnum=revnum*10+digit
    temp=temp//10

if num==revnum:
    print("the number is a palindrome")

else:
    print("number is not an palindrome")

#lcm and hcf

numl=int(input("enter the largest num"))
nums=int(input("enter the smallest num"))

while nums:
    numstr=nums
    nums=numl%nums
    numl=numstr

print("the hcf is ",numl)