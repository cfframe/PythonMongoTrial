from pymongo import MongoClient
import os
import configparser
from pprint import pprint

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))
# connect to MongoDB
connection_string = config['TRIAL']['MONGO_DB_URI']
client = MongoClient(connection_string)

# Set the db object to point to the business database
db = client.business

ASingleReview = db.reviews.find_one({})
print('A sample document:')
pprint(ASingleReview)

result = db.reviews.update_one({'_id' : ASingleReview.get('_id') }, {'$inc': {'likes': 1}})
print('Number of documents modified : ' + str(result.modified_count))

UpdatedDocument = db.reviews.find_one({'_id':ASingleReview.get('_id')})
print('The updated document:')
pprint(UpdatedDocument)
