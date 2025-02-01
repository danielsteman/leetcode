def get_exp(n, exp):
    if exp == 1:
        return n
    else:
        return n * get_exp(n, exp - 1)


if __name__ == "__main__":
    result = get_exp(3, 3)
    print(result)
