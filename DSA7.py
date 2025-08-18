# (61) First letter to appear only once in a string.
def first_non_repeating_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None  # If no non-repeating character is found

# Method 2:
def first_non_repeating_char(s):
    char={}
    for char in s:
        char[char] = char.get(char, 0) + 1
    for char in s:
        if char[char] == 1:
            return char
        
        
 # (63)  First letter to appear twice in a string
def first_repeating_char(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return char
        char_set.add(char)
    return None  # If no repeating character is found

# Method 2:
def first_repeating_char(s):
    char_set = {}
    for char in s:
        if char in char_set:
            return char
        char_set[char] = char_set.get(char, 0) + 1
    return None  # If no repeating character is found

# (63) Delete Characters to Make Fancy String
# Ex: "leeetcode" -> "leetcode"
def make_fancy_string(s):
    result = []
    for i in range(len(s)):
        if i < 2 or s[i] != s[i - 1] or s[i] != s[i - 2]:
            result.append(s[i])
    return ''.join(result)


# (64)  Find Maximum Removals From Source String
# Example 1:  Input: source = "abbaa", pattern = "aba", targetIndices = [0, 1, 2]
# Output: 2:  # Explanation: After removing characters at indices 0, 1, and 2 from "abbaa",
# we get "aa", which is not equal to "aba".
def max_removals(source, pattern, target_indices):
    for index in sorted(target_indices, reverse=True):
        source = source[:index] + source[index + 1:]
    return 1 if source == pattern else 0
