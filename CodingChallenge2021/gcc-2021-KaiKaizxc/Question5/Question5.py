
def sol(n):
    # add code

    no_of_0 = 0
    for index in range(len(n)):
        if n[index] == "0":
            no_of_0 += 1
    if no_of_0 % 2 == 0:
        return "B"
    else:
        return "A"
    # do not edit below code


def main():
    n = input()
    print(sol(n))


if __name__ == '__main__':
    main()
