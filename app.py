from itertools import product


DEFAULT_KEYBOARD = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]


def validate(keyboard, pin):
    """
    Validates keyboard and pin provided by user.
    :param keyboard: a list of lists of strings
    :param pin: a string of digits
    :return: nothing or raises ValueError if validation fails
    """
    if not all([isinstance(keyboard, list), isinstance(pin, str)]):
        raise TypeError(
            f"Input is not valid. Keyboard must be a list. Pin must be a string."
        )
    if keyboard == [] or pin == "":
        raise ValueError("Keyboard or PIN cannot be empty.")
    if not all([isinstance(row, list) for row in keyboard]):
        raise TypeError("Keyboard must be a list of lists.")
    if not all([isinstance(key, str) for row in keyboard for key in row]):
        raise TypeError("Keyboard must be a list of lists of strings.")
    if len(set(pin) - set(key for lst in keyboard for key in lst)) != 0:
        raise ValueError("Pin must contain only keys from the keyboard.")


def pin_decoder(keyboard, pin):
    """
    Returns probable pin codes using the given keyboard and observed input pin.
    Based on the observed pin, it also uses the vertical and horizontal neighbours
    of each key to build all possible permutations.
    :param keyboard: a list of lists of strings
    :param pin: a string of digits (could also decrypt a string of letters on the keyboard)
    :return: a list of strings
    """
    validate(keyboard, pin)

    # Create a list with the coordinates of the observed pin keys
    coordinates = [
        [(i, j)]
        for digit in pin
        for i in range(len(keyboard))
        for j in range(len(keyboard[i]))
        if keyboard[i][j] == digit
    ]

    # Append neighbouring keys to the list of coordinates, transform coordinates list to list of keys
    for coords in coordinates:
        key_coords = coords[0]  # Get the coordinates of the observed key
        # Replace the coordinates with the key itself
        coords[0] = keyboard[key_coords[0]][key_coords[1]]
        try:
            coords.append(keyboard[key_coords[0] + 1][key_coords[1]])
        except IndexError:
            pass
        try:
            coords.append(keyboard[key_coords[0]][key_coords[1] + 1])
        except IndexError:
            pass
        if key_coords[0] > 0:
            coords.append(keyboard[key_coords[0] - 1][key_coords[1]])
        if key_coords[1] > 0:
            coords.append(keyboard[key_coords[0]][key_coords[1] - 1])

    # Return a list of all possible combinations of the pin keys as strings
    return ["".join(x) for x in product(*coordinates)]


if __name__ == "__main__":
    user_pin = input("Enter observed pin: ")
    variations = pin_decoder(DEFAULT_KEYBOARD, user_pin)
    print("You can try the following variations:", variations)
