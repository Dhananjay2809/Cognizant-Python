(1) Two Sum Problem
#We define the function with the def
def two_sum(num,target):
    #We define a dictionary to store the numbers and their indices
    num_dict = {}
    #We iterate through the list of numbers
    # enumerate allows us to get both the index and the value
    for i, n in enumerate(num):
        #We calculate the complement of the current number
        complement = target - n
        #If the complement is already in the dictionary, we return the indices
        if complement in num_dict:
            return [num_dict[complement], i]
        #Otherwise, we add the current number and its index to the dictionary
        num_dict[n] = i
    #If no solution is found, we return an empty list
    return []
# Take input from the uset
if __name__ == "__main__":
    # Input the list of numbers
    # map is used to convert input strings to integers & split is used to separate the input by spaces
    num = list(map(int, input("Enter numbers separated by space: ").split()))
    # Input the target number
    target = int(input("Enter the target number: "))
    # Call the two_sum function and print the result
    result = two_sum(num, target)
    print("Indices of the two numbers that add up to the target:", result)
    
   


# (2) Sell and Buy stock problem
def max_profit(prices):
    # Initialize variables to track the minimum price and maximum profit
    # float('inf') is used to set an initial high value for min_price or infinity positive value
    min_price = float('inf')
    max_profit = 0
    
    # Iterate through the list of prices
    for price in prices:
        # Update the minimum price if the current price is lower
        if price < min_price:
            min_price = price
        # Calculate the profit if we sell at the current price
        profit = price - min_price
        # Update the maximum profit if the current profit is higher
        if profit > max_profit:
            max_profit = profit
            
    return max_profit
# Take input from the user
if __name__ == "__main__":
    prices=list(map(int,input("Enter stock prices separated by space: ").split()))
    result = max_profit(prices)
    print("Maximum profit from stock prices:", result)




# (3)  Contains Duplicates
def contains_duplicate(nums):
    # Use a set to track seen numbers
    seen = set()
    # Iterate through the list of numbers
    for num in nums:
        # If the number is already in the set, we have a duplicate
        if num in seen:
            return True
        # Otherwise, add the number to the set
        seen.add(num)
    # If no duplicates are found, return False
    return False



# (4) Valid Anagram
def is_anagram(s,t):
    # If the lengths of the strings are different, they cannot be anagrams
    if len(s) != len(t):
        return False
    # Sort both strings and compare them
    return sorted(s) == sorted(t)

# Take input from the user
if __name__=="__main__":
    s = input("Enter the first string: ")
    t = input("Enter the second string: ")
    result = is_anagram(s, t)
    print("Are the two strings anagrams?", result)



# (5) Intersection of Two Arrays
def intersection(nums1, nums2):
    # Convert both lists to sets to find unique elements
    set1 = set(nums1)
    set2 = set(nums2)
    # Find the intersection of both sets
    return list(set1 & set2)



# (6) Plus One
def plus_one(digits):
    # Start from the last digit and add one
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # If the digit is 9, set it to 0 and continue to the next digit
        digits[i] = 0
    # If we reach here, it means we have a carry out, so we need to add a new digit at the start
    return [1] + digits

# 🧑‍💻 User input
input_str = input("Enter digits separated by spaces (e.g. 1 2 3): ")
digits = list(map(int, input_str.strip().split()))

# ➕ Add one
result = plus_one(digits)

# 📤 Output result
print("Result after adding one:", result)




# (7) Moves Zeroes
def move_zeroes(nums):
    # Initialize a pointer for the position of the next non-zero element
    last_non_zero_index = 0
    
    # Iterate through the list
    for i in range(len(nums)):
        # If the current element is not zero, we move it to the last non-zero index
        if nums[i] != 0:
            nums[last_non_zero_index] = nums[i]
            last_non_zero_index += 1
            
    # After all non-zero elements are moved, fill the rest of the list with zeros
    for i in range(last_non_zero_index, len(nums)):
        nums[i] = 0
        
    return nums


# (8) Majority Element
def majority_element(nums):
    # Initialize a dictionary to count occurrences of each number
    count = {}
    
    # Iterate through the list of numbers
    for num in nums:
        # If the number is already in the dictionary, increment its count
        if num in count:
            count[num] += 1
        else:
            # Otherwise, add it to the dictionary with a count of 1
            count[num] = 1
            
        # If the count of the current number exceeds half the length of the list, return it
        if count[num] > len(nums) // 2:
            return num
            
    return None  # If no majority element is found



# (9)  Valid Parintheses
def is_valid(s):
    # Initialize a stack to keep track of opening parentheses
    stack = []
    # Define a mapping of closing to opening parentheses
    mapping = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the string
    for char in s:
        # If the character is a closing parenthesis
        if char in mapping:
            # Pop the top element from the stack if it's not empty, otherwise assign a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped element matches the corresponding opening parenthesis
            if mapping[char] != top_element:
                return False  # Mismatch found, return False
        else:
            # If it's an opening parenthesis, push it onto the stack
            stack.append(char)
    
    # If the stack is empty, all parentheses were matched correctly
    return not stack
    
    
    
    
    
# (10)  Merge two sorted lists
def merge_two_sorted_lists(l1, l2):
    # Initialize a dummy node to help with the merging process
    dummy = ListNode(0)
    current = dummy
    
    # While both lists have nodes to compare
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1  # Link the smaller node to the merged list
            l1 = l1.next  # Move to the next node in l1
        else:
            current.next = l2  # Link the smaller node to the merged list
            l2 = l2.next  # Move to the next node in l2
        current = current.next  # Move to the next position in the merged list
    
    # If there are remaining nodes in either list, link them
    current.next = l1 if l1 else l2
    
    return dummy.next  # Return the merged list starting from the first real node

 