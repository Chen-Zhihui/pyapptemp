
import sys
from qtpy import QtCore, QtGui, QtWidgets
from qtpy.QtCore import Qt
import pandas as pd
import datetime
import qtawesome as qta

COLORS = ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0', '#f7f7f7', '#fddbc7', '#f4a582', '#d6604d', '#b2182b', '#67001f']

class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data = None):
        super(TableModel, self).__init__(None)
        self.df = data if data is not None else pd.DataFrame()

    def data_frame(self):
        return self.df

    def reset(self, data):
        self.df = data
        self.modelReset.emit()

    def data(self, index, role):
        value = self.df.iloc[index.row(), index.column()]

        if role == Qt.DisplayRole:
                    # Perform per-type checks and render accordingly.
            if isinstance(value, datetime.datetime):
                # Render time to YYY-MM-DD.
                return value.strftime("%Y-%m-%d")

            if isinstance(value, float):
                # Render float to 2 dp
                return "%.2f" % value

            if isinstance(value, str):
                # Render strings with quotes
                return '%s' % value

            if isinstance(value, bool):
                return "{}".format(value)

            # Default (anything not captured above: e.g. int)
            return str(value)

        if role == Qt.EditRole:
            return str(value)

        # color blocks
        # if role == Qt.DecorationRole:
        #     if (isinstance(value, int) or isinstance(value, float)):
        #         value = int(value)

        #         # Limit to range -5 ... +5, then convert to 0..10
        #         value = max(-5, value)  # values < -5 become -5
        #         value = min(5, value)   # valaues > +5 become +5
        #         value = value + 5       # -5 becomes 0, +5 becomes + 10

        #         return QtGui.QColor(COLORS[value])
            
        #     else:
        #         return None

        # if role == Qt.TextAlignmentRole:
        #     if isinstance(value, int) or isinstance(value, float):
        #         # Align right, vertical middle.
        #         return Qt.AlignVCenter + Qt.AlignRight

        # if role == Qt.ForegroundRole:
        #     if (
        #         (isinstance(value, int) or isinstance(value, float))
        #         and value < 0
        #     ):
        #         return QtGui.QColor('red')

        # if role == Qt.BackgroundRole:
        #     if (isinstance(value, int) or isinstance(value, float)):
        #         value = int(value)  # Convert to integer for indexing.

        #         # Limit to range -5 ... +5, then convert to 0..10
        #         value = max(-5, value) # values < -5 become -5
        #         value = min(5, value)  # valaues > +5 become +5
        #         value = value + 5     # -5 becomes 0, +5 becomes + 10

        #         return QtGui.QColor(COLORS[value])

            # if index.column() == 2:
            #     # See below for the data structure.
            #     return QtGui.QColor('blue')
        return None


    def rowCount(self, index):
        return self.df.shape[0]

    def columnCount(self, index):
        return self.df.shape[1]
    
    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.df.columns[section])

            if orientation == Qt.Vertical:
                return str(self.df.index[section])


    # def flags(self, index) :
    #     if index.isValid():
    #         return Qt.ItemIsEditable
    #     return super(TableModel, self).flags(index) | Qt.ItemIsEditable

class SampleTable(QtWidgets.QTableView) :

    def __init__(self) -> None:

        super().__init__()

        data = pd.DataFrame([
            [1, 9, 2],
            [1, 0, -1],
            [3, 5, 2],
            [3, 3, 2],
            [5, 8, 9],
            ], 
            columns = ['A', 'B', 'C'], 
            index=['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5']
            )        

        self.table_model = TableModel(data)        
        self.setModel(self.table_model)
        self.verticalHeader().setMaximumWidth(0)

        self.setWindowIcon(qta.icon('mdi.view-list',
                        color='blue',
                        color_active='orange')
                        )


if __name__ == "__main__":
    class MainWindow(QtWidgets.QMainWindow):

        def __init__(self):
            super().__init__()
            self.table = SampleTable()
            self.setCentralWidget(self.table)


    app=QtWidgets.QApplication(sys.argv)
    window=MainWindow()
    window.resize(1200, 800)
    window.show()
    app.exec_()