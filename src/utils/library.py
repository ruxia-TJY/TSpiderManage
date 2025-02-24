'''
    utils/library.py

    library class
'''
import os.path

from utils.network import *
from utils.utils import *
import utils.app as TSpider
from utils.spider import *

class TSpiderLibrary:
    def __init__(self):
        self.library:dict = {}
        self.name:str = ''
        self.description:str = ''
        self.path:str = ''
        self.update:bool = False
        self.type:LibraryType = LibraryType.LOCAL_FILE
        self.spider_list:list = []


    def update_data(self) -> [bool,None|str]:
        '''
        parse and scan for class
        :return: bool,None|str. True,None if success;and False error otherwise
        '''
        if self.type == LibraryType.LOCAL_FILE:
            status,message = load_json_from_file(os.path.join(TSpider.LIBRARY_PATH,self.path))
        elif self.type == LibraryType.WEB_FILE:
            status, message = load_json_from_string(download_json(self.path))
        else:
            status,message = False,'Not valid type'
        if not status:
            return False,message

        self.library = message
        self.name = self.library['static']['name']
        self.description = self.library['static']['description']
        self.update = self.library['static']['update']
        self.spider_list = [Spider(i) for i in self.library['library']]
        return True,None

    def get_spider_name_list(self) -> list:
        '''
        get spider name
        :return: spider name list
        '''
        return [i.name for i in self.spider_list]

    def get_spider_by_name(self,name:str) -> [bool,None|Spider]:
        '''
        search for spider by name
        :param name: spider name
        :return: True,Spider if found,False,None if not
        '''
        status,message = False,None
        for spider in self.spider_list:
            if spider.name == name:
                status,message = True,spider
        return status,message
