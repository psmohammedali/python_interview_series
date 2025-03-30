try:
    n1 = int(input())
    n2 = int(input())
    val = n1/n2

except ValueError:
    print("valueError")

else:
    print("No except")

finally:
    print("Printing finally")