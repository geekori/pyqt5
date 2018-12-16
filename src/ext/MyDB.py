'''

操作SQLite数据库

'''

import sys

from PyQt5.QtSql import QSqlDatabase,QSqlQuery

def createDB():
    db = QSqlDatabase.addDatabase('QSQLITE')
    # 指定SQLite数据库的文件名
    db.setDatabaseName('./db/database.db')
    if not db.open():
        print('无法建立与数据库的连接')
        return False
    query = QSqlQuery()
    query.exec('create table people(id int primary key,name varchar(10),address varchar(50))')
    query.exec('insert into people values(1,"李宁","Shenyang")')
    query.exec('insert into people values(2,"超人","克星")')
    db.close()
    return True

if __name__ == '__main__':
    createDB()