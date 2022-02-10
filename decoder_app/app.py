from itertools import product


def pin_decoder(keyboard: list[list[str]], pin: str) -> list[str]:
    """
    Returns probable pin codes using the given keyboard and observed input pin.
    :param keyboard: a list of lists of strings
    :param pin: a string of digits (could also decrypt a string of letters on the keyboard)
    :return: a list of strings
    """

    # Check if the pin is valid
    if type(pin) != str:
        raise ValueError(f"{pin} is not a valid PIN. PIN must be a string of digits")
    if not pin.isdigit():
        raise ValueError(f"{pin} is not a valid PIN. PIN string must be made of digits")

    # Create a list with the coordinates of the observed pin keys
    coordinates = [[(i, j)] for digit in pin for i in range(len(keyboard)) for j in
                   range(len(keyboard[i])) if keyboard[i][j] == digit]

    # Append neighbouring keys to the list of coordinates, transform coordinates list to list of keys
    for coords in coordinates:
        key_coords = coords[0]  # Get the coordinates of the observed key
        coords[0] = keyboard[key_coords[0]][key_coords[1]]  # Replace the coordinates with the key itself
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
