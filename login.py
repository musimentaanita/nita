from datetime import MAXYEAR
import sys
from PyQt5 import QtWidgets,QtGui, QtCore, uic
from login1 import Ui_MainWindow
from login1 import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox, QLabel
import MySQLdb as mysql
from Register import Ui_RegisterWindow
from Register import *
from homepage import Ui_homepage
from homepage import *


class HomePage(QtWidgets.QMainWindow,Ui_homepage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("HOME PAGE")
        
class Register_Window(QtWidgets.QMainWindow,Ui_RegisterWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("REGISTER SCREEN")
        
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.w = Register_Window()
        self.h = HomePage()
        
        self.setWindowTitle("Login Screen")
        
        self.loginBtn.clicked.connect(self.loginbutton)
        self.cancelBtn.clicked.connect(self.cancelbutton)
        self.createAcctBtn.clicked.connect(self.createAcct)
            
    def loginbutton(self):
    
            user_name = self.nameEdit.text()
            pass_word = self.passEdit.text()
        
            host = '127.0.0.1'
            user = 'root'
            password = ''
        
            try:
                mydb = mysql.connect(host,user,password)
                cur = mydb.cursor()
            
                cur.execute('show databases')
                print(cur.fetchall())
            
                db_select = 'use DIMS'
                cur.execute(db_select)
                
                desc_tb = "desc login"
                cur.execute(desc_tb)
                print(cur.fetchall())

                insert_tb = "insert into login(username,password) values('Anita','12345');"
                cur.execute(insert_tb)
                print(cur.fetchall())
                
                select_tb = "select username, password from login"
                cur.execute(select_tb)
                print(cur.fetchall())
                
                tb_select = "select username, password from login where username = '" + user_name + "' and password = '" + pass_word + "';"
                cur.execute(tb_select)
                result = cur.fetchone()
                
                select_tb = "select username, password from login"
                cur.execute(select_tb)
                print(cur.fetchall())

                if result == None:
                    print("Invalid login credentials")
                    
                else:
                    self.h.show()
            
            except mysql.Error:
                print('Failed to connect to the database')
            finally:
                mydb.close()
         
    def cancelbutton(self):
        sys.exit()
        
    def createAcct(self,checked):
            self.w.show() 
              
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()