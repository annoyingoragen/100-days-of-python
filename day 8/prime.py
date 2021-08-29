def primenum(num):
    is_prime=True
    for i in range(2,num):
        if num % i==0:
            is_prime=False
    if is_prime:
        print("The number is prime")
    else :
        print("it's not a prime")

number= int(input("Enter a number: "))

primenum(number)
