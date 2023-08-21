
import math
import os
from tqdm import tqdm

number = int(input("Enter a number till when we will check for prime.(minimum 4)"))
prime_list = [2,3]


def clear_screen():
    # Call clear screen command based on the OS
    os.system('cls' if os.name=='nt' else 'clear')

for i in tqdm(range(4,number)):
    # Check if it's an even
    if i % 2 != 0:
        is_prime = True
        check_till = int(math.sqrt(i))
        for j in range(2, check_till+1):
            if i % j == 0:
                # Not a prime number
                is_prime = False
                break
        if is_prime: prime_list.append(i)

print(f"All numbers that are prime till {number}:  {prime_list}")

