from pymongo import MongoClient,errors

__author__ = 'xeosted'


uri = 'mongodb://localhost:27017/'


dbName = 'EOSmain'

class EOSdb:
    def __init__(self,uri,clientName):

        self.client = MongoClient(uri)

        self.db = self.client[clientName]

    def eosAccounts(args):
        return self.db.Accounts.find_one({'name': 'marcin'})


    def test(db):

        print(db.collection_names(include_system_collections=False))

        print(db.Accounts.find_one())

        print(db.Accounts.find_one({'name': 'marcin'}))


        print(db.Transactions.find_one())

        print(db.Actions.find_one())

        print(db.Blocks.find_one({'block_num': 100}))

        try:
            for insert_change in db.Blocks.watch():
                print(insert_change)
        except errors.PyMongoError:
            # The ChangeStream encountered an unrecoverable error or the
            # resume attempt failed to recreate the cursor.
            print('...')