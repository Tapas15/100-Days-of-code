

def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1, 2):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

prime_checker(30000000)