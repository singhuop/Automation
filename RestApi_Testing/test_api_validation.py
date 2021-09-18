import requests
import json
from Utilities import configuration
from Utilities import resource
from Utilities import payload

def test_single_user():
    url_single=configuration.getConfig()['API']['endpoint']+resource.ApiResources.single_user
    request_json=requests.get(url_single)
    json_data=request_json.json()
    print(json_data)
    assert request_json.status_code==200
    assert json_data['data']['email']=='janet.weaver@reqres.in'

def test_list_user():
    url_list=configuration.getConfig()['API']['endpoint']+resource.ApiResources.list_user
    request_json = requests.get(url_list)
    json_data = request_json.json()
    for i in json_data['data']:
        print(i['id'])
        if i['id']==7:
            assert i['id'] ==7
            assert i['email']=='michael.lawson@reqres.in'
            assert i['first_name']== 'Michael'
            assert i['last_name'] == 'Lawson'
            break

def test_no_user():
    url_no_usr = configuration.getConfig()['API']['endpoint'] + resource.ApiResources.no_user
    request_json = requests.get(url_no_usr)
    json_data = request_json.json()
    assert request_json.status_code==404

def test_post_create():
    post_url=configuration.getConfig()['API']['endpoint']+resource.ApiResources.post_create
    request_json=requests.post(post_url,json=payload.post_create_user())
    print(request_json.status_code)
    json_data=request_json.json()
    print(json_data)


def test_post_create_from_db():
    post_url = configuration.getConfig()['API']['endpoint'] + resource.ApiResources.post_create
    query="select * from gaurds"
    request_json=requests.post(post_url,json=payload.post_data_from_db(query))
    print(request_json.status_code)
    json_data = request_json.json()
    print(json_data)
