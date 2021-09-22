def printDivisors(n) : 
    i = 1
    bag = []
    while i <= n : 
        if (n % i==0) : 
            bag.append(i)
        i = i + 1
    return bag
    
# Driver method 
print("The divisors of 100 are: ")
print(printDivisors(100))