__author__ = 'pr0c'

import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['test']
collection = database['students']

students = [student for student in collection.find({}) if student['mark'] == 99]

print(students)