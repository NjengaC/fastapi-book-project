import py_compile


def test_main_syntax():
    # This will raise an error if main.py has any syntax errors
    py_compile.compile("main.py", doraise=True)
