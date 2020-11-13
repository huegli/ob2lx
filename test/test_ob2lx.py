from ob2lx.ob2lx import convert_l2o

TESTCONTENT = "Hello World"


def test_l2o() -> None:
    assert convert_l2o(TESTCONTENT) == TESTCONTENT + chr(13)
