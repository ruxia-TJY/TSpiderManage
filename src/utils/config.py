'''
    utils/config.py

    config file operation
'''
from utils.utils import *

class LibraryConfig:
    '''
        library in config file
    '''
    def __init__(self,name,path,type):
        self.name = name
        self.path = path
        if type == 'local file':
            self.type = LibraryType.LOCAL_FILE
        elif type == 'web file':
            self.type = LibraryType.WEB_FILE

class Config:
    '''
    config file
    '''
    def __init__(self):
        self.config:dict = {}
        self.config_file_path:str = 'config.json'

        self.is_update:bool = True
        self.default_library:LibraryConfig = None


    def read_config_file(self) -> bool:
        '''
        read config file
        :return: bool
        '''
        status,self.config = load_json_from_file(self.config_file_path)
        if not status:
            return False

        self.parse_config()
        return True

    def parse_config(self) -> None:
        '''
        parse config dict
        :return:
        '''
        self.is_update = self.config['update']['enable']
        self.default_library = LibraryConfig(self.config['default']['library']['name'],
                                             self.config['default']['library']['path'],
                                             self.config['default']['library']['type'])