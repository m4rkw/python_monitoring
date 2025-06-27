#!/usr/bin/env python3

import os
import sys

version = os.popen("pip index versions m4rkw-lambda-tracing 2>/dev/null |egrep '^Available' |cut -d ' ' -f3 |cut -d ',' -f1").read().rstrip()
ex = version.split('.')
n = int(ex[-1]) + 1

version = '.'.join(ex[:-1]) + '.' + str(n)

content = open('pyproject.toml').read().replace('VERSION', version)

with open('pyproject.toml','w') as f:
    f.write(content)

with open('version','w') as f:
    f.write(version)
