from collections import ChainMap
from datetime import datetime, timezone


# merging two dict's
d1 = {'one': 1}
d2 = {'two': 2}
merged = ChainMap(d1, d2)

# PEP 584 update operator
d3 = {'one': 1}
d3 |= [('two', 2)]

# PEP 584 merge operator
d4 = {'one': 1}
d5 = {'two': 2}
d4 = d4 | d5

# suffix prefix removers
s = 'Hello World from Python 3.9!'
without_prefix = s.removeprefix('Hello World ')
without_suffix = s.removesuffix('Python 3.9!')

# times
datetime(2020, 2, 22, 12, 0).astimezone()
datetime(2020, 2, 22, 12, 0).astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
datetime(2020, 2, 22, 12, 0).astimezone(timezone.utc)
