from ui.uimain import Ui_MainWindow

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from utils import app as TSpider

class UipyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(UipyMainWindow, self).__init__(parent=None)
        self.setupUi(self)

        self.tW_list_header = ["名称","作者","版权","更新日期","状态"]
        self.tW_list.setColumnCount(len(self.tW_list_header))

        self.tW_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tW_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tW_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tW_list.setHorizontalHeaderLabels(self.tW_list_header)

        self.tW_list.setRowCount(len(TSpider.TSpider_library.spider_list))

        for col_index,spider in enumerate(TSpider.TSpider_library.spider_list):
            list = [spider.name,spider.author,spider.license,spider.update]
            for row_index,spider_item in enumerate(list):
                item = QTableWidgetItem(list[row_index])
                item.setTextAlignment(Qt.AlignCenter)
                self.tW_list.setItem(col_index,row_index,item)