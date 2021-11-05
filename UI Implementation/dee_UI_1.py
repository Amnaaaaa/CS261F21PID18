#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas  as pd
import csv

class Ui_Dialog(object):
    
    #def __init__(self):
        #self.loadData()
    #def loadData(self):
        
        #df = pd.read_csv("C:\\Users\\MAHNOOR SHAD\\Desktop\\midproject\\CS261F21PID18\\medicineScrapping.csv")
        #row = 0
        #self.tableWidget.setRowCount(len(df))
        #for d in df:
            #self.tableWidget.setItem(row,0,QiWidgetsQTableWidgetItem(q["Name"]))
            #print(1)
            #row = row+1
#         print(df)
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 570)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 751, 571))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(72, 155, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 751, 16))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(142, 193, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 10, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 10, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(40, 320, 571, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.loaddata()
        
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 320, 571, 21))
#         self.label_2.setObjectName("label_2")
#        self.verticalScrollBar = QtWidgets.QScrollBar(self.frame)
 #       self.verticalScrollBar.setGeometry(QtCore.QRect(590, 340, 16, 171))
  #      self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
   #     self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(630, 520, 101, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(520, 30, 221, 251))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(194, 222, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 151, 31))
        self.comboBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 90, 151, 31))
        self.comboBox_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 140, 151, 31))
        self.comboBox_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 200, 75, 23))
        self.pushButton_6.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(160, 80, 171, 20))
        self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(194, 222, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_3.setObjectName("label_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 130, 271, 51))
        self.plainTextEdit.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(194, 222, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(200, 220, 91, 23))
        self.pushButton_7.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(194, 222, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "                                                                                      CURE VIBE"))
        self.pushButton.setText(_translate("Dialog", "Start"))
        self.pushButton_2.setText(_translate("Dialog", "Pause"))
        self.pushButton_3.setText(_translate("Dialog", "Resume"))
        self.pushButton_4.setText(_translate("Dialog", "Stop"))
        self.label_2.setText(_translate("Dialog", "     Product Name          Quantity          Price          Description          Category          Discount          Ingredients"))
        self.pushButton_5.setText(_translate("Dialog", "EXIT"))
        self.comboBox.setItemText(0, _translate("Dialog", "Algorithms"))
        self.comboBox.setItemText(1, _translate("Dialog", "Insertion sort"))
        self.comboBox.setItemText(2, _translate("Dialog", "Merge sort"))
        self.comboBox.setItemText(3, _translate("Dialog", "Bubble sort"))
        self.comboBox.setItemText(4, _translate("Dialog", "Selection sort"))
        self.comboBox.setItemText(5, _translate("Dialog", "Hybrid sort"))
        self.comboBox.setItemText(6, _translate("Dialog", "Bucket sort"))
        self.comboBox.setItemText(7, _translate("Dialog", "Radix sort"))
        self.comboBox.setItemText(8, _translate("Dialog", "Counting sort"))
        self.comboBox.setItemText(9, _translate("Dialog", "Quick sort"))
        self.comboBox.setItemText(10, _translate("Dialog", "Heap sort"))
        self.comboBox.setItemText(11, _translate("Dialog", "Timsort"))
        self.comboBox.setItemText(12, _translate("Dialog", "Tree sort"))
        self.comboBox.setItemText(13, _translate("Dialog", "Cube sort"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Order"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Ascending Order"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Descending Order"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "Attributes"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "Product Name"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "Quantity"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "Price"))
        self.comboBox_3.setItemText(4, _translate("Dialog", "Description"))
        self.comboBox_3.setItemText(5, _translate("Dialog", "Category"))
        self.comboBox_3.setItemText(6, _translate("Dialog", "Discount"))
        self.comboBox_3.setItemText(7, _translate("Dialog", "Ingredients"))
        self.pushButton_6.setText(_translate("Dialog", "RUN"))
        self.label_3.setText(_translate("Dialog", "            SEARCH "))
        self.plainTextEdit.setPlainText(_translate("Dialog", "Enter Product Name....\n"
""))
        self.pushButton_7.setText(_translate("Dialog", "Search"))
    def loaddata(self):
        # f = open('medicineScrapping.csv', 'r')
        
        df = pd.read_csv("medicineScrapping.csv",encoding = 'utf8')
        reader = df.values.tolist()
        
        # print("No Read")
        
#         JobTitle=[]
        
        
#         for row in reader:
#             # print(row[0])
#             JobTitle.append(row[1])
           
 
        row=0
        
        self.tableWidget.setRowCount(len(reader))
        self.tableWidget.setColumnCount(7)
        print(reader[0])
        # print(JobTitle)
        for title in reader:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title[0]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(title[1]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(title[2]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(title[3]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(title[4]))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(title[5])))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(title[6]))
#             self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(title[7]))
            row=row+1
#import login1
    
if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    
    ui = Ui_Dialog()
    ui.setupUi(Form)
    Form.show()
#     loadData()
    sys.exit(app.exec_())
    


# In[ ]:





# In[ ]:




