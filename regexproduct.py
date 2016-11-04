import re
import string
import itertools

regex = r"{[^}]*}"

test_str = "{Valery,Jason,Peter} was in {good,bad} mood and he went to the {beach, party, library}"

matches = re.finditer(regex, test_str)

subst = "{}"

# You can manually specify the number of replacements by changing the 4th argument
shell = re.sub(regex, subst, test_str, 0)

groups = []
for match in matches:
	groups.append(match.group().translate(None, '{} ').split(','))

z = itertools.product(*groups)
for a in z:
	print shell.format(*a)