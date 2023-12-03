
####Demo Video URL:
    https://youtu.be/VeMiLKF3igM

####Description:
    Qoutes is a terminal-based game that has three difficulties(easy, medium and hard), it randomly chooses a famous qoute from a famous movie -according to google- and outputs said Qoute while expecting the user aka player to guess the movie name -case-insensitively-.
    each correct answer increases the player's score by one (strive for a perfect score people).
    the game consists of a main function and additional functions like:
    chech_score, choose_lvl, choose_dif and more. These functions are called from the main function in the respective order to control the flow of the game.
    some functions return random outputs like generate_qoute, or return a long dict of qoutes and movie names like list_maker, so they are no included in the tests.

####Project Requirements:
    The project must be implemented in Python.
    It should have a main function and at least three other functions, each accompanied by tests that can be executed with pytest.
    The main function should be in a file called project.py, located in the root folder of the project.
    The three required custom functions (other than the main function) should also be in project.py and defined at the same indentation level as the main function.
    The test functions should be in a file called test_project.py, also located in the root folder of the project. The test functions should have the same name as the custom functions, prepended with test_.
    Additional classes and functions can be implemented as desired.
    Any pip-installable libraries required by the project should be listed, one per line, in a file called requirements.txt in the root of the project.
