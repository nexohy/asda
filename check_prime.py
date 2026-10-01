def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_number():
    num = input("Enter a number: ")  
    return num

if __name__ == "__main__":
    number = get_number()
    result = is_prime(number)
    print(f"Is {number} prime? {result}")
