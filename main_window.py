from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pandas as pd
import numpy as np
from combo_box import ExtendedComboBox


def translate_ui(MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "excel表格"))


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()
        self.comboBox = None
        self.pushButton = None
        self.centralWidget = None
        self.tableWidget = None
        self.setupUi(self)
        translate_ui(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        translate_ui(MainWindow)

        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(100, 150, 1000, 700))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setStyleSheet("selection-background-color:pink")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.raise_()

        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 50, 120, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("打开")

        self.comboBox = ExtendedComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(350, 50, 400, 50))
        self.comboBox.setObjectName("comboBox")
        l = ["", "公司1", "2asd", "3ewqr", "3ewqc", "2wqpu", "1kjijhm", "4kjndw", "5ioijb", "6eolv", "11ofmsw"]
        self.comboBox.addItems(l)
        MainWindow.setCentralWidget(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.openfile)
        self.pushButton.clicked.connect(self.creat_table_show)

    def openfile(self):

        # 获取路径===================================================================

        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Excel files(*.xlsx , *.xls)')

        # print(openfile_name)
        global path_openfile_name

        # 获取路径====================================================================

        path_openfile_name = openfile_name[0]

    def creat_table_show(self):
        # ===========读取表格，转换表格，===========================================
        if len(path_openfile_name) > 0:
            input_table = pd.read_excel(path_openfile_name)
            # print(input_table)
            input_table_rows = input_table.shape[0]
            input_table_columns = input_table.shape[1]
            # print(input_table_rows)
            # print(input_table_columns)
            input_table_header = input_table.columns.values.tolist()
            # print(input_table_header)

            # ===========读取表格，转换表格，============================================
            # ======================给tablewidget设置行列表头============================

            self.tableWidget.setColumnCount(input_table_columns)
            self.tableWidget.setRowCount(input_table_rows)
            self.tableWidget.setHorizontalHeaderLabels(input_table_header)

            # ======================给tablewidget设置行列表头============================

            # ================遍历表格每个元素，同时添加到tablewidget中========================
            for i in range(input_table_rows):
                input_table_rows_values = input_table.iloc[[i]]
                # print(input_table_rows_values)
                input_table_rows_values_array = np.array(input_table_rows_values)
                input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
                # print(input_table_rows_values_list)
                for j in range(input_table_columns):
                    input_table_items_list = input_table_rows_values_list[j]
                    # print(input_table_items_list)
                    # print(type(input_table_items_list))

                    # ==============将遍历的元素添加到tablewidget中并显示=======================

                    input_table_items = str(input_table_items_list)
                    newItem = QTableWidgetItem(input_table_items)
                    newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(i, j, newItem)

                    # ================遍历表格每个元素，同时添加到tablewidget中========================
        else:
            self.centralWidget.show()
