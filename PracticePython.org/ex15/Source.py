def get_string(text="Give me a string: "):
    return (input(text))


def reverse_string():
    return " ".join((get_string().split())[::-1])


print(reverse_string())