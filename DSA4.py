# (31) Word count in a string  
# Example: "Hello world" -> 2
def word_count(s):
    # Split the string by whitespace and filter out empty strings
    words = s.split()
    return len(words)


# (32)  Check for Anagram 
Example: "listen" and "silent" are anagrams
def are_anagrams(str1, str2):
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)


# (33)  Longest Word in a sentence
Ex:ample: "The quick brown fox" -> "quick"
#Method 1
def longest_word(sentence):
    # Split the sentence into words and find the longest one
    words = sentence.split()
    return max(words, key=len)

# Method 2
def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest



# (34) Check if a string is a palindrome
# Example: "racecar" is a palindrome
def is_palindrome(s):
    # Normalize the string by removing spaces and converting to lowercase
    s = s.replace(" ", "").lower()
    return s == s[::-1]


# (35)  Diagonal Sum of Matrix
# Example: [[1, 2], [3, 4]] -> 5 (1 + 4)
# Add one diagonal element at a time
def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]  # Add the main diagonal element
    return total
#Add both diagonals
def diagonal_sum(mat):
    m = len(mat)         # Number of rows
    n = len(mat[0])      # Number of columns
    total = 0
    for i in range(m):
        for j in range(n):
            if i == j:
                total += mat[i][j]  # Main diagonal
            if i != j and i + j == n - 1:
                total += mat[i][j]  # Secondary diagonal (avoid double-counting)
    return total
# 🔹 Input from user
print("Enter number of rows:")
m = int(input())

print("Enter number of columns:")
n = int(input())

print(f"Enter the matrix row by row (each row should have {n} space-separated integers):")
matrix = []
for i in range(m):
    row = list(map(int, input().split()))
    if len(row) != n:
        print(f"Error: Row {i+1} must have exactly {n} elements.")
        exit()
    matrix.append(row)

# 🔹 Compute and print result
result = diagonal_sum(matrix)
print("Sum of both diagonals:", result)



#(36)  Check Even/Odd Without % 
def is_even(num):
    return (num & 1) == 0
def is_odd(num):
    return (num & 1) == 1

# (37) Count Set Bits
# Example: 5 (binary 101) has 2 set bits
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1  # Increment count if the last bit is set
        n >>= 1         # Right shift to check the next bit
    return count
    


# (38)Sum of All Array Elements
Example: [1, 2, 3] -> 6
def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
# Method 2
def sum_of_array(arr):
    return sum(arr)  # Using built-in sum function for simplicity



# (39) Find Missing Number
def find_missing_number(arr, n):
    total = n * (n + 1) // 2  # Sum of first n natural numbers
    return total - sum(arr)   # Subtract the sum of the array from the total

# (40) Capitalize First Letter
# Example: "hello world" -> "Hello World"
def capitalize_first_letter(s):
    return ' '.join(word.capitalize() for word in s.split())

# Method 2
def capitalize_first_letter(s):
    words = s.split()
    capitalized_words = []
    for word in words:
        if word:  # Check if the word is not empty
            capitalized_words.append(word[0].upper() + word[1:])
        else:
            capitalized_words.append(word)  # Keep empty words as they are
    return ' '.join(capitalized_words)


# (41) Find Largest of Three Numbers
def largest_of_three(a, b, c):
    return max(a, b, c)