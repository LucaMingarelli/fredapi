"""  Created on 05/05/2024::
------------- _update_version_badge.py -------------

Only to be run in CI/CD.
 
**Authors**: L. Mingarelli
"""
import os


VERSION = (os.popen("""grep "version" fredapi/version.py | cut -d "'" -f 2""")
           .read()
           .strip('\n'))


with open('README.md', 'r') as f:
    README = f.read()

VERSION_BADGE_STRING = [e for e in README.split('\n') if 'https://img.shields.io/badge/version' in e][0]
VERSION_BADGE_STRING_NEW = f'[![version](https://img.shields.io/badge/version-{VERSION}-success.svg)](#)'

README_NEW = README.replace(VERSION_BADGE_STRING, VERSION_BADGE_STRING_NEW)

with open('README.md', 'w') as f:
    f.write(README_NEW)

os.system(f"""git commit -m "GitHub Workflow: Version badge updated to version={VERSION}" """)


