def isPrime(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True

fltrObj=filter(isPrime, range(50))
print ('Prime numbers between 1-50:', list(fltrObj))