from greet import greet, main


def test_greet_name() -> None:
    assert greet("Ada") == "Hello, Ada!"


def test_greet_blank_defaults_to_world() -> None:
    assert greet("  ") == "Hello, world!"


def test_main_prints(capsys) -> None:
    assert main(["Bob"]) == 0
    assert capsys.readouterr().out == "Hello, Bob!\n"
