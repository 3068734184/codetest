import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(lst):
    prime_list = []
    for num in lst:
        if is_prime(num):
            prime_list.append(num)
    return prime_list

def main():
    input_list = [23, 10, 7, 45, 67, 89, 101, 3, 56, 31]
    prime_numbers = find_primes(input_list)
    print("Prime numbers in the list are:")
    for prime in prime_numbers:
        print(prime)

if __name__ == "__main__":
    main()
