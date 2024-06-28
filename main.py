def main():
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """

    previous_value = int(input ())
    numbers.append(previous_value)

    while (True):
        current_value = int(input ())

        if current_value <= previous_value:
            numbers.append(current_value)
            previous_value = current_value
        else:
            break



    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
