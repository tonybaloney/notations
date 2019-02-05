from notations import notation

def my_example_function(arg1, arg2):
    f = 0
    for a in arg1:
        for i in a:
            f+=1
    for b in arg2:
        for j in b:
            f+=1

print(notation(my_example_function))