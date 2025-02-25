'''
    utils/spider.py

    spider class
'''
from enum import Enum


class SpiderType(Enum):
    CODE_TYPE = 0
    APPLICATION_TYPE = 1

    @classmethod
    def get_type(cls,name):
        if name == "code":
            return cls.CODE_TYPE
        elif name == "application":
            return cls.APPLICATION_TYPE


class Spider:
    '''
    Spider class
    '''
    def __init__(self,spider):
        self.name:str = spider['name']
        self.description:str = spider['description']
        self.author:str = spider['author']
        self.update:bool =spider['update']
        self.type:SpiderType = SpiderType.get_type(spider['type'])
        self.license:str = spider['license']
        self.files:dict[str,str] = spider['files']
        self.run:list[str] = spider['run']
        self.status:str = None

    def run(self):
        # TODO run spider
        pass
