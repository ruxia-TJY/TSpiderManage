'''
    utils.py

    some definition and general utility functions
'''
import json
from enum import Enum



class LibraryType(Enum):
    '''
    library type
    for examples, Type LOCAL_FILE means file in local.
    '''
    NONE_TYPE = 0
    LOCAL_FILE = 1
    WEB_FILE = 2

    @classmethod
    def get_type(cls,name):
        if name == 'local file':
            return cls.LOCAL_FILE
        elif name == 'web file':
            return cls.WEB_FILE
        else:
            return cls.NONE_TYPE

def load_json_from_file(filename:str) -> [bool, dict|str]:
    '''
    load json from file
    :param filename: json file name
    :return: json dict
    '''
    status,data = False,None
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            json_dict = json.loads(f.read())
        status,data = True,json_dict
    except Exception as e:
        statu,data = False,str(e)
    return status, data

def load_json_from_string(json_string:str) -> [bool, dict|str]:
    '''
    load json from string
    :param json_string:
    :return:
    '''
    status,data = False,None
    try:
        json_dict = json.loads(json_string)
        status = True,json_dict
    except Exception as e:
        status,data = False,str(e)
    return status, data