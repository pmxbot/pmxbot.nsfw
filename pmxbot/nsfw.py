import re

import pmxbot


def is_safe(channel, message):
	"""
	>>> pmxbot.config = {'exclude patterns': ['offensive word']}
	>>> is_safe('#inane', 'some phrase')
	True
	>>> is_safe('#inane', "don't any of you say an offensive word")
	False
	"""
	return not any(
		re.search(pattern, message)
		for pattern in pmxbot.config.get('exclude patterns', [])
	)
