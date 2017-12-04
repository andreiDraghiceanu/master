x = input("Enter the number: ")
number = int(x)

def prime(n):
    count = 0
    for i in range(1, (n+1)): 
         if n % i == 0: 
             count += 1
    if count > 2:
        print ("Not a prime")
    else:
        print ("A prime")

prime(number)
