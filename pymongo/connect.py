from pymongo import MongoClient


class DB:

    def __init__(self):
        self.createClient()

    def createClient(self):
        username = "root"
        password = "p[p[P{P{"
        self.client = MongoClient('mongodb://%s:%s@localhost:27017/' % (username, password))

    def pushData(self, collection, data):
        if isinstance(data, list):
            self.client[collection].insert_many(data)
        else:
            self.client[collection].insert_one(data)

    # collection.find(filter, projection, limit=#)

    # pipeline = [{
    #     '$match': {
    #         'origin': 'ATL',
    #         'dest': 'BOS',
    #         'dayofweek': 3
    #     }
    # }, {
    #     '$group': {
    #         '_id': {
    #             'origin': '$origin',
    #             'destination': '$dest'
    #         },
    #         'Failure': {
    #             '$sum': {
    #                 '$cond': [{
    #                     '$eq': ['$cancelled', 1]
    #                 }, 1, 0]
    #             }
    #         },
    #         'Success': {
    #             '$sum': {
    #                 '$cond': [{
    #                     '$eq': ['$cancelled', 0]
    #                 }, 1, 0]
    #             }
    #         },
    #         'Total': {
    #             '$sum': 1
    #         }
    #     }
    # }, {
    #     '$project': {
    #         'Failure': 1,
    #         'Success': 1,
    #         'Total': 1,
    #         'FailPercent': {
    #             '$divide': ['$Failure', '$Total']
    #         }
    #     }
    # }, {
    #     '$sort': SON([('_id.origin', 1), ('_id.destination', 1)])
    # }]
    # collection.aggregate(pipeline)
