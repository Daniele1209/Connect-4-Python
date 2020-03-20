def valid_input(input):
    try:
        input = int(input)
    except ValueError:
        print("Input is not valid ! ")

    if input < 1 or input > 7:
        raise ValueError("Input not valid ! ")