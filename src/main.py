'''
    TSpiderManage

    to manage spiders
'''
import os
import sys
from uipy.uimain import UipyMainWindow
from PyQt5.QtWidgets import *
from utils.library import TSpiderLibrary
from utils import app as TSpider
from utils.config import *

def init() -> None:
    '''
    do some initialization
    :return: None
    '''
    # check config.json file exist
    if not os.path.exists('config.json'):
        # TODO some operation if file config.json not exist
        return None

    # make and read config
    config = Config()
    config.read_config_file()

    # scan library list
    for file in os.listdir(TSpider.LIBRARY_PATH):
        TSpider.library_file_list.append(file)

    # try to read default library
    if config.default_library.name not in TSpider.library_file_list:
        # TODO default library json file not exist
        pass


    # read default library file
    TSpider.TSpider_library =TSpiderLibrary()
    TSpider.TSpider_library.type = LibraryType.LOCAL_FILE
    TSpider.TSpider_library.path = config.default_library.path
    TSpider.TSpider_library.update_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    init()

    uimain = UipyMainWindow()
    uimain.show()

    sys.exit(app.exec_())