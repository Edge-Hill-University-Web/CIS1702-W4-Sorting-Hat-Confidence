from sorting_hat_confidence import determine_house_by_confidence


def test_nine_is_gryffindor():
    assert determine_house_by_confidence(9) == "Gryffindor"


def test_boundary_eight_is_gryffindor():
    assert determine_house_by_confidence(8) == "Gryffindor"


def test_seven_is_ravenclaw():
    assert determine_house_by_confidence(7) == "Ravenclaw"


def test_boundary_six_is_ravenclaw():
    assert determine_house_by_confidence(6) == "Ravenclaw"


def test_five_is_hufflepuff():
    assert determine_house_by_confidence(5) == "Hufflepuff"


def test_boundary_four_is_hufflepuff():
    assert determine_house_by_confidence(4) == "Hufflepuff"


def test_three_is_slytherin():
    assert determine_house_by_confidence(3) == "Slytherin"


def test_boundary_zero_is_slytherin():
    assert determine_house_by_confidence(0) == "Slytherin"


def test_above_ten_is_invalid():
    assert determine_house_by_confidence(11) == "Invalid score"


def test_negative_is_invalid():
    assert determine_house_by_confidence(-1) == "Invalid score"
