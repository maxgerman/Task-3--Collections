import pytest
from collections_fw import unique_chars

typical_param = [
	('abbbccdf', 3),
	('aaaaaa', 0),
	('abcdefg', 7),
	('abcdeee', 4),
	('abc', 3),
	('abc', 3),  # to incr. the hits counter

]


def test_unique_chars_typical():
	for inp_val, out_val in typical_param:
		assert unique_chars(inp_val) == out_val


def test_unique_chars_atypical():
	with pytest.raises(TypeError):
		unique_chars(123)

def test_lru_cache_hits():
	'''check if cache is hitting'''
	assert unique_chars.cache_info()[0] > 0