#!/usr/bin/env python3

import os
import sys

version = os.popen("curl -s https://pypi.org/pypi/m4rkw-lambda-tracing/json | jq -r '.info.version'").read().strip()
ex = version.split('.')
n = int(ex[-1]) + 1

version = '.'.join(ex[:-1]) + '.' + str(n)

content = open('pyproject.toml').read().replace('VERSION', version)

with open('pyproject.toml','w') as f:
    f.write(content)
