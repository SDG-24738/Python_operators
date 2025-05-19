Mark1 = int(input("Enter the marks for subject 1"))
Mark2 = int(input("Enter the marks for subject 2"))
Mark3 = int(input("Enter the marks for subject 3"))
Mark4 = int(input("Enter the marks for subject 4"))
Mark5 = int(input("Enter the marks for subject 5"))
average = (Mark1 + Mark2 + Mark3 + Mark4 + Mark5)/5
if average >90:
    print("You got A*")
elif average >80:
    print("You got A")
elif average >70:
    print("You got B")
elif average >60:
    print("You got C")
elif average >50:
    print("You got D")
else:
    print("You got E")