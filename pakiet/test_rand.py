def test_some(random_number_generator):
    a = random_number_generator()
    b = 10
    assert a + b >= 15


def test_tmp(tmp_path):
    f = tmp_path.joinpath("test.txt")
    f.write_text("test")
    print("PLIK", f)
    fread = tmp_path.joinpath("test.txt")
    assert fread.read_text() == "test"
