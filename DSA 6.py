# (52)  Find the majority element (appears > n/2 times).
# Ex: [1, 2, 3, 2, 2] -> 2
def find_majority_element(arr):
    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Verify if candidate is actually the majority element
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None



# (53) Print a right triangle pattern of *.
def right_triangle_pattern(n):
    for i in range(1, n + 1):
        print('*' * i) 
        
        
        
# (54) Print Pascal’s Triangle.
def pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    for row in triangle:
        print(' '.join(map(str, row)))
        
    
    
# (55) Print a number spiral matrix.
def spiral_matrix_traversal(matrix):
    result = []
    if not matrix:
        return result
    
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            
    return result



# (56)  Rotate a matrix by 90°.
def rotate_matrix_90(matrix):
    if not matrix or not matrix[0]:
        return []
    
    n = len(matrix)
    m = len(matrix[0])
    
    # Create a new matrix for the rotated result
    rotated = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            rotated[j][n - 1 - i] = matrix[i][j]
    
    return rotated


# (57) Factorial using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# (58) Fibonacci series using recursion.
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_series = fibonacci_recursive(n - 1)
    fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series
        
        
        
# (59) Check if parentheses are balanced. using stack.
def are_parentheses_balanced(s):
    stack = []
    parentheses_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in parentheses_map.values():
            stack.append(char)
        elif char in parentheses_map.keys():
            if not stack or stack[-1] != parentheses_map[char]:
                return False
            stack.pop()
    
    return len(stack) == 0



# (60) Find next greater element for each element in array.
def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n  # Initialize result with -1
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)

    return result




# (61)  Reverse a queue.
from collections import deque
def reverse_queue(queue):
    stack = []
    
    # Transfer elements from queue to stack
    while queue:
        stack.append(queue.popleft())
    
    # Transfer elements back to queue in reverse order
    while stack:
        queue.append(stack.pop())
    
    return queue



# (62 )Implement stack using list in Python.
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    
    