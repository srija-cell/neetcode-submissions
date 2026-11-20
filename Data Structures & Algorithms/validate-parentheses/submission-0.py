class Solution:
    def isValid(self, s: str) -> bool:
        paren_stack = []
        mapping = {"]":"[", "}":"{",")":"("}
        for i in s:
            #opening bracket append in stack.
            if i in mapping.values():
                paren_stack.append(i)
            #check closing bracket check value with last stacked value. if 
            #same, true.also check if stack is empty
            elif i in mapping:
                if not paren_stack or mapping[i] != paren_stack[-1]: 
                    return False
                paren_stack.pop() #popping out the paired ones to check other
        return not paren_stack #this for checking if there is any string left
        #if we are pooping then paren_stack is empty which is True and valid but
        #if paren_stack is not empty then it is going to return invalid..
