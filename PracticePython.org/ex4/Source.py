num=int(input("Give me a number to print all of divisors: "))
divisors=[]
for x in range(1,num+1):
        if (num%x==0):
                divisors.append(x)

print(divisors)