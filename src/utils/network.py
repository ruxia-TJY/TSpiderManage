'''
    utils/network.py

    network functions
'''
import requests

def download_json(url:str) -> [bool, str]:
    '''
    download json from url
    :param url: json url
    :return: status,message if success: True,json value else: False,error message
    '''
    status,message = True,''
    try:
        response = requests.get(url)
        if response.status_code == 200:
            message = response.text
        else:
            status,message = False,str(response.status_code)
    except Exception as e:
        status,message = False,str(e)
    return status,message