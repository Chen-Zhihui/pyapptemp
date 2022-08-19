
from requests import head
from main.python.widget import zero_space, plain_frame
from qtpy.QtWidgets import (
    QPushButton, 
    QLabel, 
    QFrame, 
    QListWidget,
    QTableWidget,
    QTableWidgetItem
)

class Box(QFrame):

    def __init__(self, parent=None, flags=None) -> None:
        super(QFrame, self).__init__(parent)


class ListBox(QListWidget):

    def __init__(self, parent=None, flags=None) -> None:
        super(QListWidget, self).__init__(parent)

        # self.horizontalHeader().set
        self.addItems(["Item-1", "Item-2", "Item-3", "Item-4", "Item-5"])


class TableBox(QTableWidget):

    def __init__(self, parent=None, flags=None) -> None:
        super(QTableWidget, self).__init__(parent)
        self.horizontalHeader().setStretchLastSection(True)

        def create_header():
            items = [
                QTableWidgetItem("选中"),
                # QTableWidgetItem(m.rejected), # rejected mark
                QTableWidgetItem("目标ID"),
                QTableWidgetItem("景数据ID"),
                QTableWidgetItem("距离"),
                QTableWidgetItem("云量(%)"),
                QTableWidgetItem("拍摄日期"),
                QTableWidgetItem("分辨率"),
                QTableWidgetItem("文件路径"),        
            ]            
            return items # todo ret list<QTableWidgetItem>   
        headers = create_header()

        self.setColumnCount(len(headers))

        c= 0
        for item in headers:
            self.setHorizontalHeaderItem(c, item)
            c += 1
        
        def create_items():
            items = [
                QTableWidgetItem("选中"),
                QTableWidgetItem("目标ID"),
                QTableWidgetItem("景数据ID"),
                QTableWidgetItem("距离"),
                QTableWidgetItem("云量(%)"),
                QTableWidgetItem("拍摄日期"),
                QTableWidgetItem("分辨率"),
                QTableWidgetItem("文件路径"),        
            ]            
            return items # todo ret list<QTableWidgetItem>  

        c = 10
        self.setRowCount(c)
        for i in range(10):
            items = create_items()
            c=0
            for item in items :
                self.setItem(i, c, item)
                c += 1


        

    
