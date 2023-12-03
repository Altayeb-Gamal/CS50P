math = input("Expression: ")
x, y, z = math.split(" ")

match y:
    case "+":
        num = float(x) + float(z)
        num = "{:.1f}".format(num)
        print(num)
    case "-":
        num = float(x) - float(z)
        num = "{:.1f}".format(num)
        print(num)
    case "*":
        num = float(x) * float(z)
        num = "{:.1f}".format(num)
        print(num)
    case "/":
        num = float(x) / float(z)
        num = "{:.1f}".format(num)
        print(num)




