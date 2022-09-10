import re

import sys
import re

import sys, re
l = ['zabcz',
"zzz",
"zzxzz",
"zz",
"zxz",
"zzxzxxz"]
exp = re.compile("z...z")
for i in filter(lambda line: exp.search(line), l):
    print(i)

print(*filter(lambda line: exp.search(line), l))