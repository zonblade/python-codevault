# used for django and other.
# pip3 install pymongo
from pymongo import MongoClient

# definisikan nama database
def db_name(name='db_name'):
  return name

# buat handler supaya lebih simpel di file lain!
def mongod():
  client  = MongoClient(
                  host      = '*',
                  port      = int(1000),
                  username  = '*',
                  password  = '*'
            )
  handler = client[db_name()]
  return handler
