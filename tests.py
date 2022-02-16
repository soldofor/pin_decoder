from app import pin_decoder

keyboard = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]


def test_app():
    test_pairs = [("13", ["22", "16", "12", "43", "46", "42", "23", "26", "13"]), ("1", ["2", "4", "1"]),
                  ("3", ["3", "6", "2"]),
                  ("23", ["23", "26", "22", "53", "56", "52", "33", "36", "32", "13", "16", "12"])]
    for pair in test_pairs:
        assert sorted(pin_decoder(keyboard, pair[0])) == sorted(
            pair[1]), f"Wrong result for keyboard = {keyboard} and PIN = {pair[0]}"

    # test case (belongs to a test scenario -- flat keyboard ["1".."9"]) -> valid
    # test case (belongs to a test scenario -- matrix keyboard ["1".."3"] ["4" .. "6"])
    # test case (belongs to a test scenario -- pin value not in keyboard, valid keyboard)


if __name__ == "__main__":
    test_app()
    print("All tests passed")
