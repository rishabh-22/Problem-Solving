import os
import sys

os.environ['ENV'] = 'Demo'
# sys.path.append('python3 /home/rishabh/Documents/Devops/devops2/export.py')
import export

print(os.environ.get('RDS_DB_NAME'))
print(os.environ['RDS_DB_PASS'])
