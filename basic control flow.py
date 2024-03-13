#If and Else
def allPrimesUpTo(num):
    primes=[2]
    for x in range(3,num):
        squareRoot=x**0.5
        for number in primes:
            if x%number ==0:
                break
            if number>squareRoot:
                primes.append(x)
                break
    
    print(primes)

allPrimesUpTo(1000)