from pymongo import MongoClient
import os
import configparser
config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))
# connect to MongoDB
connection_string = config['TRIAL']['MONGO_DB_URI']
client = MongoClient(connection_string)

# Set the db object to point to the business database
db = client.business

# Showcasing the count() method of find, count the total number of 5 ratings
# print('The number of 5 star reviews using deprecated count():')
# fiveStarCount = db.reviews.find({'rating': 5}).count()

print('The number of 5 star reviews using newer alternative:')
fiveStarCount = db.reviews.count_documents({'rating': 5})
print(fiveStarCount)

# Now let's use the aggregation framework to sum the occurrence of each rating across the entire data set
print('\nThe sum of each rating occurrence across all data grouped by rating ')
starGroup = db.reviews.aggregate(
    # The Aggregation Pipeline is defined as an array of different operations
    [
        # The first stage in this pipe is to group data
        {'$group':
            {
                '_id': "$rating",
                "counter":
                {'$sum': 1}
            }
        },
        # The second stage in this pipe is to sort the data
        {"$sort": {"_id": 1}
        }
        # Close the array with the ] tag
    ])

# Print the result
for group in starGroup:
    print(group)
