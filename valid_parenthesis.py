"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""

def isValidPar(s: str) -> bool:
    # Mapping closing brackets to their opening brackets
    par_map = { ')': '(', ']': '[', '}': '{' }
    print(par_map.keys())
    print(par_map.values())
    # Instanciating stack to track brackets
    stack = []
    for char in s:
        # Checking only parenthesis skipping other chars
        if char in par_map.keys() or char in par_map.values():
            # Checking if we have closing bracket
            if char in par_map:
                # If stack has something taking the top element otherwise assigning dummy value 
                top = stack.pop() if stack else '#'
                # If top element is not open bracket of the same type then all expression is invalid
                if par_map[char] != top:
                    return False
            # If we have opening bracket adding it to the stack
            else:
                stack.append(char)
        else:
            continue
    # If all brackets were paired stack is empty and eval to False -> returning not stack which is True
    return not stack

print(isValidPar('(abba){babba}[12321]()()(){{{aaa[[[]]]}}}}'))