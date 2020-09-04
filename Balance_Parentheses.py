# class Stack(object):
#     def __init__(self):
#         self.stack = []

#     def isEmpty(self):
#         return self.stack == []

#     def push(self,element):
#         self.stack.append(element)

#     def pop(self):
#         self.stack.pop

def Check_Balance_Parentheses(s):
    opening = ['[','{','(']
    match = (('(',')'),('{','}'),('[',']'))
    stack = []
    if(len(s)%2!=0 or not s):
        return False
    for i in s:
        if i in opening:
            stack.append(i)
        else:
            previous = stack.pop()
            if((previous,i) not in match):
                return False
    return len(stack)==0
            


print(Check_Balance_Parentheses('))'))