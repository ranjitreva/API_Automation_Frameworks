import json


def GET(sessions_object, url, headers):
    response = sessions_object.get(url, headers=headers)
    print('------------------------------Printing Request-----------------------------')
    print(f'URL : {url}')
    print(f'Headers : {headers}')
    print('---------------------------Printing Response Status Code--------------------')
    print(f'Status Code : {response.status_code}')
    print('----------------------------Printing Response Body---------------------------')
    print(f'Response Body : {json.dumps(response.json(), indent=4)}')
    return response


def POST(sessions_object, url, headers, payload):
    response = sessions_object.post(url, headers=headers, json=payload)
    print('------------------------------Printing Request-----------------------------')
    print(f'URL : {url}')
    print(f'Headers : {headers}')
    print(f'Payload : {payload}')
    print('---------------------------Printing Response Status Code--------------------')
    print(f'Status Code : {response.status_code}')
    print('----------------------------Printing Response Body---------------------------')
    print(f'Response Body : {json.dumps(response.json(), indent=4)}')
    return response


def DELETE(sessions_object, url, headers):
    response = sessions_object.delete(url, headers=headers)
    print('------------------------------Printing Request-----------------------------')
    print(f'URL : {url}')
    print(f'Headers : {headers}')
    print('---------------------------Printing Response Status Code--------------------')
    print(f'Status Code : {response.status_code}')
    return response


#  def print_request(url, headers, payload=None):
#     print('------------------------- Printing Request ---------------------------')
#     print(f'URL : {url}')
#     print(f'Headers : {headers}')
#     print(f'Payload : {payload}')
#
# def print_response(response):
#     print('-----------------------Printing Response Status Code-------------------')
#     print(f'Status Code : {response.status_code}')
#     print('-----------------------Printing Response Body--------------------------')
#     print(f'Response Body : {json.dumps(response.json(), indent=4)}')
