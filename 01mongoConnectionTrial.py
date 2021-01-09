from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
import dns

# Need both 'os' and 'configparser' to use .ini file
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

# connect to MongoDB
connection_string = config['TRIAL']['MONGO_DB_URI']
if connection_string.find('<user>:<password>'):
    print("Update .ini with user, password and target mongoDB instance.")
else:
    client = MongoClient(connection_string)
    db = client.admin
    # Issue the serverStatus command and print the results
    serverStatusResult = db.command("serverStatus")
    pprint(serverStatusResult)
