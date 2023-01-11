sign = "+"
a = input()
while not sign == "=":
    sign = input()
    b = input()
    if sign ==  "+":
        result = int(a)+int(b)
    if sign == "-":
        result = int(a)-int(b)
    if sign == "*":
        result = int(a)*int(b)
    if sign == "/":
        result = int(a)/int(b)
    if sign == "%":
        result = int(a)%int(b)
        if result == 0:
            result = int(a)/int(b)
            else:
                result = int(a)/int(b) + " rest " + int(a)%int(b)
    if sign == "^":
        result = int(a)**int(b)
    a = result
    print (a)