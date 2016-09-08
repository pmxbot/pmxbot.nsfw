import re

import pmxbot


def is_safe(channel, message):
	return not any(
		re.search(pattern, message)
		for pattern in pmxbot.config.get('exclude patterns', [])
	)
