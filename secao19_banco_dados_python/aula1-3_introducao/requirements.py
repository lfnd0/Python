#! python

try:
    from mysql import connector
except ModuleNotFoundError:
    print('MySQL Connector not installed')
else:
    print('MySQL Connector installed')
