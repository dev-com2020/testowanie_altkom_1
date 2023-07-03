
def myapp():
    print("Aplikacja MyApp została uruchomiona")

def test_capsys(capsys):
    myapp()
    captured = capsys.readouterr()
    assert captured.out == "Aplikacja MyApp została uruchomiona\n"