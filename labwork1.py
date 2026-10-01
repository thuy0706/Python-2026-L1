#Exercise 1: Calculate the area of a circle
import math

radius = float(input("Enter circle radius? "))
area = math.pi * (radius ** 2)
print(f"Circle area = {area:.1f}")

#Exercise 2: Convert Celsius to Fahrenheit
celsius = float(input("Enter the temperature in Celsius? "))
fahrenheit = (celsius * 9/5) + 32
print(f"{int(celsius)} (C) = {fahrenheit:.1f} (F)")

#Exercise 3: Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number? "))
if is_prime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is a NOT prime number")

#Exercise 4: Check if a number is perfect
def is_perfect(num):
    if num < 1:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

n = int(input("Enter a number? "))
if is_perfect(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is a NOT perfect number")

#Exercise 5: Find favorite color
colors = ["red", "green", "blue", "yellow", "purple"]
color = input("Enter a color to search for? ").lower()
if color in colors:
    print(f"{color} is in the list")
else:
    print(f"{color} is not in the list")


#Exercise 6:Using range()
range1 = range(0, 7, 1)
range2 = range(1, 11, 3)
range3 = range(5, 0, -1)
range4 = range(6, -3, -2)

print("range1:", list(range1))
print("range2:", list(range2))
print("range3:", list(range3))
print("range4:", list(range4))

#Exercise 7: Remove dollar sign from a string
def remove_dollar_sign(s):
    return s.replace("$", "")


text = input("Enter a string: ")

result = remove_dollar_sign(text)

print("Result:", result)

#Exercise 8: Extract even numbers from a list
def extract_even(l):
    result = []

    for number in l:
        if number % 2 == 0:
            result.append(number)

    return result


numbers = [1, 4, 5, -1, 10]

print(extract_even(numbers))

#Exercise 9: Calculate the factorial of a number
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


n = int(input("Enter a non-negative integer: "))

print("Factorial =", factorial(n))

#Exercise 10: Find all divisors of a number
def get_divisors(n):
    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return divisors


n = int(input("Enter a number: "))

print("Divisors:", get_divisors(n))

#Exercise 11: Calculate the distance between two points
import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

print("Distance =", distance(x1, y1, x2, y2))

#Exercise 12: Print a pattern of stars
def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


m = 4
n = 5

print_pattern(m, n)