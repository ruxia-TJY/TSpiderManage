'''
    utils/spider.py

    spider class
'''

class Spider:
    '''
    Spider class
    '''
    def __init__(self,spider):
        self.name = spider['name']
        self.description = spider['description']
        self.author = spider['author']
        self.update =spider['update']
        self.type = spider['type']
        self.license = spider['license']
        self.files = spider['files']
        self.run = spider['run']

    def run(self):
        # TODO run spider
        pass
