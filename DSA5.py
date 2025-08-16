# (42)  Count Even and Odd numbers in an array
# Example: [1, 2, 3, 4] -> (2, 2)
def count_even_odd(srr):
    n=len(arr)
    even=0
    odd=0
    for i in range(n):
        if arr[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd , even

# Inpur from user
if __name__ == "__main__":
    arr = list(map(int, input("Enter elements separated by space: ").split()))
    
    odd_count, even_count = count_even_odd(arr)
    
    print(f"Odd count: {odd_count}, Even count: {even_count}")
    
    
    
# (43)  Remove Duplicates from String
# Ex: "hello" -> "helo"
def remove_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)



# (44) Rotate Array Left
# Example: [1, 2, 3, 4] with k=2 -> [3, 4, 1, 2]
def rotate_array_left(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is larger than n
    return arr[k:] + arr[:k]
    
# Rotate Array Right
# Ex : [2, 4, 1,3] with k=1 -> [3, 2, 4, 1]
def rotate_array_right(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is larger than n
    return arr[-k:] + arr[:-k]


# (45) Reverse Digits
# Ex: 1234 -> 4321
def reverse_digits(n):
    return int(str(n)[::-1])
# Method 2
def reverse_digits(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num


# Spiral Matrix Traversal
# Example: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] -> [1, 2, 3, 6, 9, 8, 7, 4, 5]
def spiral_matrix_traversal(matrix):
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            # Traverse from right to left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            
        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            
    return result

#Input from user
if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    matrix = []
    print(f"Enter the matrix row by row (each row should have {cols} space-separated integers):")
    for _ in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print(f"Error: Each row must have exactly {cols} elements.")
            exit()
        matrix.append(row)
    
    result = spiral_matrix_traversal(matrix)
    print("Spiral order traversal:", result)
    
    
    
    # (46) Print Alternate Elements
    # Example: [1, 2, 3, 4, 5] -> [1, 3, 5]
def print_alternate_elements(arr):
    return arr[::2]
# :: 2 means take every second element starting from index 0


# (47) Segregate 0s and 1s
# Ex: [0, 1, 0, 1, 0] -> [0, 0, 0, 1, 1]
def segregate_zeros_and_ones(arr):
    zero_count = arr.count(0)
    one_count = len(arr) - zero_count
    return [0] * zero_count + [1] * one_count

# method 2
def segregate_zeros_and_ones(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        while left < right and arr[left] == 0:
            left += 1
        while left < right and arr[right] == 1:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    return arr

# Method 3 (sorting)
def segregate_zeros_and_ones(arr):
    return sorted(arr)


# (48)  Find Peak Element
# Ex: [1, 3, 20, 4, 1] -> 20
def find_peak_element(arr):
    n = len(arr)
    if n == 0:
        return None
    if n == 1 or arr[0] >= arr[1]:
        return arr[0]
    if arr[n - 1] >= arr[n - 2]:
        return arr[n - 1]
    
    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return arr[i]
    
    return None

# Method 2
def find_peak_element(arr):
    n = len(arr)
    if n == 0:
        return None
    
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return arr[left]


# (49)  Count Digits That Divide Number
# Example: 1012 -> 3 (1, 1, 2)
def count_dividing_digits(n):
    count = 0
    original_n = n
    while n > 0:
        digit = n % 10
        if digit != 0 and original_n % digit == 0:
            count += 1
        n //= 10
    return count


# (50)  Count Vowels and Consonants in a String
# Example: "Hello World" -> (3, 7)
def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return vowel_count, consonant_count


# (51) Chech array is sorted or not
# Example: [1, 2, 3, 4] -> True
def is_sorted(arr):
    return arr == sorted(arr)





