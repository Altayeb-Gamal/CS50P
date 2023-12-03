from project import choose_dif, check_score, get_lvl

qoutes = {
    "Toto, I've got a feeling we're not in Kansas anymore": "WIZARD OF OZ",
    "Here's looking at you, kid": "CASABLANCA",
    "I'm going to make him an offer he can't refuse": "SCHINDLER'S LIST",
}


def test_get_lvl():
    assert get_lvl("easy") == 5
    assert get_lvl("medium") == 3
    assert get_lvl("hard") == 1


def test_check_score():
    assert check_score(5, "easy") == "Well done, perfect score"
    assert check_score(5, "medium") == "Well done, perfect score"
    assert check_score(5, "hard") == "Well done, perfect score"


def test_choose_dif():
    assert choose_dif("easy") == 5
    assert choose_dif("medium") == 5
    assert choose_dif("hard") == 5
