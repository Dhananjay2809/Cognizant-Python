# (11) Find missing number
# Input: nums = [3, 0, 1] → Output: 2
 def find_missing_number(nums):
        # Calculate the expected sum of numbers from 0 to n
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    
    # Calculate the actual sum of the numbers in the list
    actual_sum = sum(nums)
    
    # The missing number is the difference between the expected and actual sums
    return expected_sum - actual_sum
# Method 2
def missingNumber(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)




# (12)  Find Duplicates Elements in the List
#a = [1, 2, 3, 4, 5, 2, 6, 3]
#print(find_duplicates(a))  # Output: [2, 3]


 def find_duplicates(nums):
    # Use a set to track seen numbers
    seen = set()
    duplicates = []
    
    # Iterate through the list of numbers
    for num in nums:
        # If the number is already in the set, it's a duplicate
        if num in seen:
            duplicates.append(num)
        else:
            # Otherwise, add the number to the set
            seen.add(num)
    
    return duplicates



#(13)  Count vowel and consonant
text = "Hello World!"
print("Vowels:", vowels)         # Output: 3
print("Consonants:", consonants) # Output: 7

def count_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return vowel_count, consonant_count
# 🚀 Main Program
if __name__ == "__main__":
    user_input = input("Enter a string: ")
    vowels, consonants = count_vowels_consonants(user_input)

    print("\n🔍 Analysis Result:")
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    
    
   
   
   
    # (14)   FizzBuzz Variation
    
def fizzbuzz_variation(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
    


# (15)   Sort array without using built-in sort
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already sorted, so we can skip them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



# (16)  Count Odd number in an array

# Metod 1
     def count_odd_numbers(arr):
        return len([num for num in arr if num % 2 != 0])
# Method 2
def count_odd_numbers(arr):
    count = 0
    for num in arr:
        if num % 2 != 0:
            count += 1
    return count


# (17)  Remove the string spaces

#method 1--Remove All Spaces (including between words)
def remove_all_spaces(text):
    return text.replace(" ", "")
# Method 2--Remove Leading and Trailing Spaces
def remove_leading_trailing_spaces(text):
    return text.strip()



# (18) Largest and Smallest Number in an array

def find_largest_and_smallest(arr):
    if not arr:
        return None, None  # Handle empty array case
    largest = smallest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    return largest, smallest
  
  #Method 2
def find_largest_and_smallest(arr):
    if not arr:
        return None, None  # Handle empty array case
    largest = max(arr)
    smallest = min(arr)
    return largest, smallest


# (19)  Palindrom check string
def is_palindrome(s):
    # Normalize the string by removing spaces and converting to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

#Method 2
def is_palindrome(s):
    # Normalize the string by removing spaces and converting to lowercase
    s = ''.join(s.split()).lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Palindrome Number
def is_palindrome_number(num):
    # Convert the number to string and check if it reads the same forwards and backwards
    return str(num) == str(num)[::-1]
# Method 2
def is_palindrome_number(n):
    original = n
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return original == reversed_num


# (20)  Armstrong Number
def is_armstrong_number(num):
    # Convert the number to string to easily iterate over digits
    str_num = str(num)
    num_digits = len(str_num)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in str_num)
    
    # Check if the sum equals the original number
    return armstrong_sum == num

# Method 2 by the while loop
def is_armstrong_number(n):
    original = n
    sum_of_powers = 0
    num_digits = len(str(n))

    while n > 0:
        digit = n % 10
        sum_of_powers += digit ** num_digits
        n //= 10

    return original == sum_of_powers


