import re

my_pattern = r"^\s*((?:It's|Some|Maybe)[\w\s,']+(?:[.?]))\s*$"
my_regex = re.compile(my_pattern, re.M)

