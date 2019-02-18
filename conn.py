import pymysql

# class Conn:

#     def __init__(self):
#         self.host='localhost',
#         self.user='root',
#         self.passwd='root',
#         self.db='organisation',
#         self.mydb=None


def getconn():
    global mydb

    mydb=pymysql.connect(host='localhost', user='root', passwd='root', db='organisation')

    print('hoorray!')
    return mydb

# c=Conn()
getconn()

