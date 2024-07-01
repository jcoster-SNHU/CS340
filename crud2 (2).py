from pymongo import MongoClient
from bson.objectid import ObjectId

# Class definition of animal shelter object
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        #
        # Connection Variables
        #
        self.USER = USER
        self.PASS = PASS
        self.HOST = HOST
        self.PORT = PORT
        self.DB = DB
        self.COL = COL
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]
    
    # Method which is used to insert a document into animals collection
    def create(self, doc):
        # Validate method parameters
        if doc is None:
            raise Exception('\nERROR: No valid data was specified.')

        # Attempt to insert data
        inserted = self.collection.insert_one(doc)    
        if inserted is None:
            raise Exception('\nERROR: Failed to insert document: %s' % (doc))

    # Method which is used to read records from animals collection
    def read(self, filter=None):
        if filter is None:
            raise Exception('\nERROR: No valid data was specified.')

        # Retrieve documents by filter
        return self.collection.find(filter)
        
    # Method which is used to update records from animals collection
    def update(self, filter=None, values=None):
        # Validate method parameters
        if filter is None:
            raise Exception('\nERROR: No valid filter was specified.')
        if values is None:
            raise Exception('\nERROR: No valid values were specified.')  
        
        # Update records based on specified filter and values
        updated = self.collection.update_one(filter, values)
        if updated is None:
            raise Exception('\nERROR: Failed to update document based on filter: %s' % (filter))
      
    # Method which is used to delete records in the animals collection
    def delete(self, filter=None):
        # Validate method parameters
        if filter is None:
            raise Exception('\nERROR: No valid filter was specified.')

        # Delete records based on specified filter
        deleted = self.collection.delete_many(filter)
        if deleted is None:
            raise Exception('\nERROR: Failed to delete records based on filter: %s' % (filter))

