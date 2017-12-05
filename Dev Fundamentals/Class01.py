def is_prime(n):
    div = 1
    counter = 0
    if counter == 0:
        return False
    while (div <= n/2):
        if(n % div == 0):
            return False
        div +=1

    return True
        if (counter > 1):
            return False

        div += 1
    return counter == 1
if __name__=="__main__":
    print("5 is prime:"+str(is_prime(5)))
    print(is_prime(11))
    print(is_prime(1))
    print(is_prime(354654600000000000000000000000000000))
