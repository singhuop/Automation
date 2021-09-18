from Utilities.configuration import getQuery
def post_create_user():
    body = {
    "name": "babulal",
    "job": "chowkidar"
}
    return body

def post_data_from_db(query):
    body = {}
    tp = getQuery(query)
    body['name'] = tp[0]
    body['job'] = tp[1]
    return body
