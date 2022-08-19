from qtpy.QtWidgets import QSizePolicy

from qtpy.QtWidgets import (
    QLayout, 
    QFrame, 
    QTableView,
    QSizePolicy, 
    QTreeWidget, 
    QTreeWidgetItem,
    QTabWidget,
    QHBoxLayout
)
from qtpy.QtCore import (
    QModelIndex,
)

def zero_space(layout: QLayout):
    layout.setSpacing(0)
    layout.setContentsMargins(0,0,0,0)

def plain_frame(frame: QFrame) :
    frame.setFrameShape(QFrame.NoFrame)
    frame.setFrameShadow(QFrame.Plain)

def create_vline():
    vLine = QFrame()        
    vLine.setFrameShape(QFrame.VLine)        
    vLine.setFrameShadow(QFrame.Plain)
    vLine.setProperty("qss_vline", True)
    vLine.setMaximumWidth(1)
    return vLine

def create_hline():
    vLine = QFrame()        
    vLine.setFrameShape(QFrame.HLine)        
    vLine.setFrameShadow(QFrame.Plain)
    vLine.setProperty("qss_hline", True)
    vLine.setMaximumHeight(1)
    return vLine

def set_table_style(table):
    plain_frame(table)
    table.horizontalHeader().setStretchLastSection(True)
    table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    table.setAlternatingRowColors(True)

def create_table(parent): 
    fileTable = QTableView(parent)
    set_table_style(fileTable)
    return fileTable

def create_tree_widget(parent):
    treeView = QTreeWidget(parent)  
    treeView.setAlternatingRowColors(True)      
    plain_frame(treeView)
    return treeView

def fill_sample_tree(tree):
    tree.setHeaderLabel(" 指标体系 ")
    root = QTreeWidgetItem(tree)

    root.setText(0, "通信系统效能")

    group1 = QTreeWidgetItem(root)
    group1.setText(0, "通信能力")

    subItem11 = QTreeWidgetItem(group1)        
    subItem11.setText(0, "信道容量")

    subItem12 = QTreeWidgetItem(group1)
    subItem12.setText(0, "通信模式")

    subItem13 = QTreeWidgetItem(group1)
    subItem13.setText(0, "通信距离")

    subItem14 = QTreeWidgetItem(group1)
    subItem14.setText(0, "误码率")

    subItem15 = QTreeWidgetItem(group1)
    subItem15.setText(0, "电磁环境")

    group2 = QTreeWidgetItem(root)
    group2.setText(0, "机动能力")

    subItem22 = QTreeWidgetItem(group2)
    subItem22.setText(0, "航向")

    subItem23 = QTreeWidgetItem(group2)
    subItem23.setText(0, "航速")

    tree.expandAll()

def create_tree_widget_sample(parent):
    tree = create_tree_widget(parent)
    fill_sample_tree(tree)
    return tree

def create_tab_widget(parent):
    tab = QTabWidget(parent)
    return tab

def wrapped_tabwidget(parent):
    container = QFrame(parent)
    layout = QHBoxLayout(container)
    zero_space(layout)
    tabs = create_tab_widget(container)
    layout.addWidget(tabs)
    return tabs, container

def set_table_header_width(table):
    col = table.model().columnCount(QModelIndex())
    twidth = table.width()
    hwidth = table.verticalHeader().width() if table.verticalHeader().isVisible() else 0
    width = (table.width() - 20 - hwidth)/col
    for i in range(col):
        table.horizontalHeader().resizeSection(i, width)

class Stretch(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.addStretch()