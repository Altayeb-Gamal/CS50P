def get_input(prompt):
    while True:
        try:
            s = input(prompt)
        except (ValueError, KeyError):
            pass
        else:
            return s
help(any)