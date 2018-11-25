# -*- coding: utf-8 -*-

from PyQt5.QtCore import *

from PyQt5.QtWidgets import QWidget,QMessageBox

class MySharedObject(QObject):

	@pyqtSlot(int,int,result=int,name="addInt")
	def addInt(self,a,b):
		print(b)
		return a+b
	def getStrValue( self):
		return '123'

	def setStrValue( self,  str ):
        #  
		print('获得页面参数 ：%s'% str )

    #需要定义对外发布的方法


    

