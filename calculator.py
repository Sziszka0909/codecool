def bevitel():
    szam1 = input("Enter a number (or a letter to exit): ")
    try:
        a = int(szam1)
        operator = input("Enter an operator: ")
        szam2 = input ("Enter another number: ")
        szamolas(a, operator, szam2)
    except ValueError:
        exit()

def szamolas(a, c, b):
    a = int(a)
    b = int(b)

    if c == "+":
        eredmeny = a + b
    elif c == "-":
        eredmeny = a - b
    elif c == "*":
        eredmeny = a * b
    elif c == "/":
        eredmeny = a / b
    elif c == "**":
        eredmeny = a ** b
    else:
        eredmeny ="Unknown operator"

    print("Result: " + str(eredmeny))
    print("")

while True:
    bevitel()