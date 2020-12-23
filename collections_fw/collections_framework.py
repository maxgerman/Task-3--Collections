from collections import Counter
from functools import lru_cache

@lru_cache
def unique_chars(input_string: str):
	'''returns the number of unique characters in the string; has cache'''
	if not isinstance(input_string, str):
		raise TypeError(f'String expected, got {type(input_string)}')
	c = Counter(input_string)
	ul = len([key for key, val in c.items() if val == 1])
	return ul