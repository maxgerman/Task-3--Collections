from collections import Counter

cache = {}


def unique_chars(input: str):
	'''returns the number of unique characters in the string; has cache'''
	if input in cache:
		ul = cache[input]
	else:
		c = Counter(input)
		ul = len([key for key, val in c.items() if val == 1])
		cache[input] = ul
	return ul
