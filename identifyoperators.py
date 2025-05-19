x = 10
if type(x) is int:
    print("True")
else:
    print("False")
y = 3.14
if type(y) is float:
    print("True")
else:
    print("False")
if x is not y:
    print("They have different identity")
else:
    print("They have same identity")