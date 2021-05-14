def isValid(s):
    replace = True
    while replace:
        start_length = len(s)
        for inner in ["{}", "()", "[]"]:
            s = s.replace(inner, "")
        if start_length == len(s):
            replace = False

    return s == ""

def validParantheses(s):
    stack = []
    mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for char in s:
        if char in mapping:
            if stack:
                top_elem = stack.pop()
            else:
                top_elem = "#"
            if mapping[char] != top_elem:
                return False
        else:
            stack.append(char)
    return not stack

print(validParantheses("{}[]"))

# print(isValid("[{()[]"))