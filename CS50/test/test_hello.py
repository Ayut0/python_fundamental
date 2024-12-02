from CS50.function.hello import hello

def test_default():
    assert hello() == "Hello, world!"

def test_arg():
    for name in ["Steph", "Klay", "Draymond"]:
        assert hello(name) == f"Hello, {name}!"