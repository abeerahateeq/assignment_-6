# insert a value into array at specified index
def insert_value(arr,index,value):
    arr. insert(index,value)
    return arr
# simple shopping cart programme
# Function to add item
def add_item(cart, item):
    cart.append(item)
    print("Cart after adding:", cart)

# Function to remove item
def remove_item(cart, item):
    if item in cart:
        cart.remove(item)
    print("Cart after removing:", cart)

# Function to update quantity
def update_quantity(cart, item, new_item):
    if item in cart:
        index = cart.index(item)
        cart[index] = new_item
    print("Cart after updating quantity:", cart)

# Example usage:
cart = ["apple", "banana", "orange"]
add_item(cart, "grape")
remove_item(cart, "banana")
update_quantity(cart, "grape", "grapes (2kg)")
#print first 25 integers
i = 1
while i <= 25:
    print(i)
    i += 1
#print first ten even number
i = 2
count = 0
while count < 10:
    print(i)
    i += 2
    count += 1
# factorial calculation using while loop
def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

# Example usage:
print(factorial(5))  # Output: 120
#remove negative numbers from array
numbers = [3, -2, 7, -5, 10, -1]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        numbers.pop(i)
    else:
        i += 1
print(numbers)  # Output: [3, 7, 10]
# sum of numbers in an array using while loop
def sum_of_numbers(arr):
    i = 0
    total = 0
    while i < len(arr):
        total += arr[i]
        i += 1
    return total

# Example usage:
print(sum_of_numbers([1, 2, 3, 4]))  # Output: 10
# convert celsius into fahrenheit
def celsius_to_fahrenheit(temps_celsius):
    temps_fahrenheit = []
    i = 0
    while i < len(temps_celsius):
        fahrenheit = (temps_celsius[i] * 9/5) + 32
        temps_fahrenheit.append(fahrenheit)
        i += 1
    return temps_fahrenheit

# Example usage:
temps_celsius = [0, 20, 30, 100]
print(celsius_to_fahrenheit(temps_celsius))  # Output: [32.0, 68.0, 86.0, 212.0]
# remove odd numbers from an array
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        numbers.pop(i)
    else:
        i += 1
print(numbers)  # Output: [2, 4, 6, 8, 10]