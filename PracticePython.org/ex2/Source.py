num=int(input("Give me a number:"))
check=int(input("Give me a number to divide by:"))
if (num % check==0):
    {
        print(num," is divisible by ",check)
    }
else:
    {
        print(num," don't divides evenly into ",check)
    }
if (num % 2 == 0):
    {
            print("This number is even")
    }
else:
    {
        print("This number is odd")
    }
if(num % 4 == 0):
    {
        print("This number is a multiple of 4")
    }