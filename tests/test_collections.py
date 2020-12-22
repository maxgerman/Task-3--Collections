import pytest
from collections_fw import unique_chars

typical_param = [
	('abbbccdf', 3),
	('aaaaaa', 0),
	('abcdefg', 7),
	('abcdeee', 4),

]


def test_unique_chars_typical():
	for inp_val, out_val in typical_param:
		assert unique_chars(inp_val) == out_val


def test_unique_chars_atypical():
	with pytest.raises(TypeError):
		unique_chars(123)