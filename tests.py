from app import pin_decoder

keyboard = [['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']]


def test_app():
    assert pin_decoder(keyboard, "123") == ['123', '126', '122', '153', '156', '152', '133', '136', '132', '113', '116',
                                            '112',
                                            '423', '426', '422', '453', '456', '452', '433', '436', '432', '413', '416',
                                            '412',
                                            '223', '226', '222', '253', '256', '252', '233', '236', '232', '213', '216',
                                            '212'], f"Wrong result for {keyboard} and PIN = 123"
    assert pin_decoder(keyboard, "1") == ["1", "4", "2"], f"Wrong result for {keyboard} and PIN = 1"


if __name__ == '__main__':
    test_app()
    print("All tests passed")
