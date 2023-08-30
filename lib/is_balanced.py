def is_balanced(expression):
    stack = [] 

    
    bracket_mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_mapping.values():  
            stack.append(char)
        elif char in bracket_mapping.keys():  
            if not stack or stack.pop() != bracket_mapping[char]:
                return False

    return len(stack) == 0