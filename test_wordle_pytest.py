from Wordle import Wordle


def test_no_match():
    wordle = Wordle("child", "ropes")
    # first argument is the guess, second is the target
    wordle.calculate_match()
    assert wordle.result == "00000"
