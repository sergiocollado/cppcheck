#/usr/bin/python
#
# This script analyses Cppcheck dump files to locate threadsafety issues
# - warn about static local objects
#

import cppcheckdata
import sys

def reportError(token, severity, msg):
  sys.stderr.write('[' + token.file + ':' + str(token.linenr) + '] (' + severity + ') ' + msg + '\n')

def checkstatic(data):
  for var in data.variables:
    if var.isStatic=='true' and var.isLocal=='true' and var.isClass=='true':
      reportError(var.typeStartToken, 'warning', 'Local static object')

for arg in sys.argv[1:]:
  print('Checking ' + arg + '...')
  data = cppcheckdata.parsedump(arg)
  checkstatic(data)