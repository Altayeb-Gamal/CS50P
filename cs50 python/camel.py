def main():
    camel_case = input("camelCase: ")
    snake_case(camel_case)
    print("snake_case: ", snake_case(camel_case))




def snake_case(camel_case):
    snake_case = ""
    for c in camel_case:
        if c == c.upper():
            snake_case += "_" + c.lower()
        else:
            snake_case += c
    return snake_case


main()