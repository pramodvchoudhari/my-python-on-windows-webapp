#!c:\users\pc51212\source\repos\flaskwebproject1\flaskwebproject1\pythonhelloworld\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Flask==1.1.1','console_scripts','flask'
__requires__ = 'Flask==1.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Flask==1.1.1', 'console_scripts', 'flask')()
    )
