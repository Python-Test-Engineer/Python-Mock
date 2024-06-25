# Open in own isolated project

python -m pytest -vs .\tests\test_joke.py::TestJoke::test_0100_no_patch - this returns a random joke with a corresponding random length.

python -m pytest -vs .\tests\test_joke.py::TestJoke::test_0200_len_joke

python -m pytest -vs .\tests\test_joke.py::TestJoke::test_0300_get_joke

python -m pytest -vs .\tests\test_joke.py::TestJoke::test_0400_fail_get_joke