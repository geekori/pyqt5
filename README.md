# Pyqt5示例大全
## 基础入门
[Hello world!](src/basic/First.py)  
[环境说明.txt](src/basic/搭建PyQt5开发环境.txt) 
[窗口类型.txt](src/controls/主窗口类型.txt)

## 基础组件与操作
### 组件
[复选框控件（QCheckBox）](src/controls/QCheckBoxDemo.py)  
[下拉列表控件（QComboBox）](src/controls/QComboBoxDemo.py)
[标签控件（QLabel）](src/controls/QLabelDemo.py)  
[标签与伙伴控件（QLabel）](src/controls/QLabelBuddy.py)  
[文本输入框控件（QLineEdit）](src/controls/QLineEditDemo.py)  
[文本输入框回显模式（QLineEdit）](src/controls/QLineEditEchoMode.py)    
[文本输入框校验](src/controls/QLineEditMask.py)  
[按钮组件（QPushButton等）](src/controls/QPushButtonDemo.py)  
[单选按钮控件（QRadioButton）](src/controls/QRadioButtonDemo.py)  
[滑块控件（QSlider）](src/controls/QSliderDemo.py)：可以用来完成放大缩小操作  
[计数器控件（QSpinBox）](src/controls/QSpinBoxDemo.py)  
[编辑框组件（QTextEdit）](src/controls/QTextEditDemo.py)  

### 操作
[窗口居中](src/controls/CenterForm.py)  
[状态栏消息](src/controls/FirstMainWin.py)  
[设置图标](src/controls/IconForm.py)  
[退出窗口](src/controls/QuitApplication.py)
[屏幕坐标](src/controls/ScreenGeometry.py)
[设置组件提示消息](src/controls/Tooltip.py)

## 菜单栏/工具栏/状态栏
[创建和使用菜单栏](src/menu_toolbar_statusbar/Menu.py)  
[创建和使用工具栏](src/menu_toolbar_statusbar/Toolbar.py)  
[创建和使用状态栏](src/menu_toolbar_statusbar/StatusBar.py)  

## 树/表格
### 树
[树控件（QTreeWidget）的基本用法](src/table_tree/BasicTreeWidget.py)
[显示列表数据（QListView控件）](src/table_tree/ListView.py)
[扩展的列表控件（QListWidget）](src/table_tree/ListWidget.py) 
[添加、修改和删除树控件中的节点](src/table_tree/ModifyTree.py)  
[为树节点添加响应事件](src/table_tree/TreeEvent.py)


### 表格
[扩展的表格控件（QTableWidget）](src/table_tree/TableWidget.py)
[设置单元格字体和颜色](src/table_tree/CellFontAndColor.py)
[设置单元格的文本对齐方式](src/table_tree/CellTextAlignment.py)  
[设置单元格尺寸](src/table_tree/CellSize.py)  
[合并单元格](src/table_tree/Span.py)
[在单元格中放置控件](src/table_tree/PlaceControlInCell.py)  
[按列排序](src/table_tree/ColumnSort.py)  
[改变单元格中图片的尺寸](src/table_tree/CellImageSize.py)  
[在单元格中实现图文混排的效果](src/table_tree/CellImageText.py)  
[在表格中快速定位到特定的行](src/table_tree/DataLocation.py)
[显示二维表数据（QTableView控件）](src/table_tree/TableView.py
[在表格中显示上下文菜单]()



## 对话框
[对话框：QDialog](src/dialogs/QDialogDemo.py)  
[颜色对话框：QColorDialog](src/dialogs/QColorDialog.py)  
[字体对话框：QFontDialog](src/dialogs/QColorDialog.py)  
[文件对话框：QFileDialog](src/dialogs/QFileDialogDemo.py)  
[输入对话框：QInputDialog](src/dialogs/QInputDialogDemo.py)
[消息对话框：QMessageBox](src/dialogs/QMessageBox.py)

## 日历和时间
[不同风格日历和时间 QDateTimeEdit](src/calendar_time/DateTimeEdit.py)
[日历控件](src/calendar_time/MyCalendar.py)

## 容器组件
[停靠组件](src/containers/DockWidget.py)  
[容纳多文档的窗口](src/containers/MultiWindows.py)  
[堆栈窗口控件（QStackedWidget）](src/containers/QStackedWidget.py)
> 类似于一个菜单栏，选项卡控件更像是一个横着的堆栈窗口组件

[滚动条控件（QScrollBar）](src/containers/ScrollBar.py)  
[选项卡控件：（QTabWidget）](src/containers/TabWidget.py)
## [信号与槽](src/SignalSlot/)
[入门示例](src/SignalSlot/SignalSlotDemo.py)
[信号与槽自动连接](src/SignalSlot/AutoSignalSlot.py)  
[自定义信号](src/SignalSlot/CustomSignal.py)  
[Lambda表达式](src/SignalSlot/LambdaSlotArg.py)  
[为类添加多个信号](src/SignalSlot/MultiSignal.py)  
[信号槽N对N连接与断开](src/SignalSlot/NNSignal.py)  
[Override（覆盖）槽函数](src/SignalSlot/OverrideSlot.py)
[使用Partial对象为槽函数传递参数](src/SignalSlot/PartialSlotArg.py)  
[窗口信号](src/SignalSlot/WinSignal.py)  



## 多线程
[让程序自动关闭](src/multithread/AutoCloseWindow.py)  
[计数器](src/multithread/Counter.py)  
[动态显示时间](src/multithread/ShowTime.py)  
[多线程更新UI数据](src/SignalSlot/ThreadUpdateUI.py)
