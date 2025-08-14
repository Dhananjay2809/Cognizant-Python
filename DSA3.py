# (21) Print Fibonacci Series
 # _ is used instead of a variable and it runs the loop n times outputting the Fibonacci sequence
 # end=' ' tells Python to end the print with a space instead of the default newline (\n).
def fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    fibonacci_number(n)



# (22) Reverse the Array 
# Method 1
def reverse_array(arr):
    return arr[::-1]

 #  Method : 2
 def reverse_array(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# Method 3
def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        # Swap elements
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr





# (23)  Frequency of each elemnt in an array
 def frequency_of_elements(arr):
    frequency = {}
    for elem in arr:
        if elem in frequency:
            frequency[elem] += 1
        else:
            frequency[elem] = 1
    return frequency
  if __name__ == "__main__":
        # Input from user
    arr = input("Enter elements separated by space: ").split()
    
    # Optional: Convert to integers if needed
    arr = [int(x) for x in arr]

    # Get frequency
    freq = frequency_of_elements(arr)

    # Print result
    print("Frequency of elements:")
    for key, value in freq.items():
        print(f"{key}: {value}")  
# f-strings let you insert variables directly into strings using {} braces.            
                
      


# (24)  Count Pairs With Given Sum
# It returns the only unique pairs that sum to the target value.
def count_pairs_with_sum(arr, target_sum):
    count = 0
    seen = set()
    
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            count += 1
        seen.add(num)
    
    return count
     
# It return the total number of pairs (including duplicates) that sum to the target value.     
def count_pairs_with_sum(arr, target_sum):
    count = 0
    freq = {}

    for num in arr:
        complement = target_sum - num
        if complement in freq:
            count += freq[complement]
        
        # Update frequency of current number
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return count




# (25) GCD of Two Numbersdef gcd(a, b):
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(48, 18))  # Output: 6




# (26) Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_numbers_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes



# (27)  Leader in an array
 # A Leader is an element that is greater than all of the elements on its right side in the array.
 
def find_leaders(arr):
    leaders = []
    n = len(arr)
    maxi = arr[n - 1]
    leaders.append(maxi)

    for i in range(n - 2, -1, -1):
        if arr[i] > maxi:
            maxi = arr[i]
            leaders.append(maxi)

    return leaders[::-1]  # Reverse to maintain original order



# (28) Find the second largest number in an array
# Method 1
# float('-inf') represents negative infinity. anf for positive we use float('inf') for positive infinity.
def second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements for a second largest
    first, second = float('-inf'), float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

Method 2
def second_largest_alt(arr):
    unique = list(set(arr))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]



# (29)  Toggle Case of Characters in a String
def toggle_case(s):
    toggled = []
    for char in s:
        if char.islower():
            toggled.append(char.upper())
        elif char.isupper():
            toggled.append(char.lower())
        else:
            toggled.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(toggled)

 #toggled is a list of characters (like ['h', 'E', 'L', 'L', 'O'])
# ''.join(toggled) combines them into one string: 'hELLO'





# (30)  Move All Zeros to the End of an Array
def move_zeros_to_end(arr):
    non_zero_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1
    for i in range(non_zero_index, len(arr)):
        arr[i] = 0
    return arr


# (31) Swap Two Numbers Without Using a Temporary Variable
# Method 1: Using Arithmetic Operations
def swap_numbers(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b
# Method 2: Using Bitwise XOR
def swap_numbers_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
# Method 3 : Direct Tuple Assignment
def swap_numbers_tuple(a, b):
    a, b = b, a
    return a, b