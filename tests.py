from app import pin_decoder

keyboard = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def test_app():
    assert pin_decoder(keyboard, "1") == [
        "1",
        "4",
        "2",
    ], f"Wrong result for {keyboard} and PIN = 1"

    actual_value = sorted(pin_decoder(keyboard, "123"))
    expected_value = [
        "123",
        "126",
        "122",
        "153",
        "156",
        "152",
        "133",
        "136",
        "132",
        "113",
        "116",
        "112",
        "423",
        "426",
        "422",
        "453",
        "456",
        "452",
        "433",
        "436",
        "432",
        "413",
        "416",
        "412",
        "223",
        "226",
        "222",
        "253",
        "256",
        "252",
        "233",
        "236",
        "232",
        "213",
        "212",
        "216"
    ]
    assert actual_value == sorted(expected_value), "Test case failed on pin = 123"
    # test case (belongs to a test scenario -- empty keyboard) -> error

    # test case (belongs to a test scenario -- empty pin, valid keyboard) -> empty list
    # test case (belongs to a test scenario -- flat keyboard ["1".."9"]) -> valid
    # test case (belongs to a test scenario -- matrix keyboard ["1".."3"] ["4" .. "6"])
    # test case (belongs to a test scenario -- pin value not in keyboard, valid keyboard)


if __name__ == "__main__":
    test_app()
    print("All tests passed")
