from rakshak.dbcalls.dbconfig import client,db,calls



def updates_one(filter_query,update_query):

    result = calls.update_one(filter_query, {"$set": update_query})

    return result