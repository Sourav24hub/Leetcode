class Solution(object):
    def isValid(self, s):
        di = { "(" : ")" , "[" : "]" , "{" : "}" }
        stack = []
        for i in s:
            if i in di:
                stack.append(i)
            else:
                if stack and i == di[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True