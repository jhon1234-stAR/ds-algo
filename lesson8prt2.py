# If the stack if empty- balanced bracket or else unbalanced brackets

open_list = ["(", "[", "{"]
closed_list = [")", "]", "}"]

# function to check the brackets
def check(mystring):
    stack = []
    for i in mystring:
        if i in open_list:
            stack.append(i)
        elif i in closed_list:
            pos = closed_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                print("Unbalanced expression")
                
    if len(stack) == 0:
        print("Balanced expression")
    else:
        print("Unbalanced expression")


expression = "{hello i am leon {from here}and there are many type of people the end"
check(expression)