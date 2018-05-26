__author__ = 'Maxwell Li'

import pymysql

# create DB
# db = pymysql.connect(host='localhost',user='root', password='abc123', port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()

#connection
db = pymysql.connect(host='localhost', user='root', password='abc123', port=3306, db='spiders')
cursor = db.cursor()

# create table
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()

# insert data
data = {
    'id': '20120029',
    'name': 'Mary',
    'age': 38
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)

try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
        print('Failed')
        db.rollback()
#db.close()

#update
# sql = 'UPDATE students SET age = %s WHERE name = %s'
# try:
#    cursor.execute(sql, (25, 'Bob'))
#    db.commit()
# except:
#    db.rollback()
# db.close()

# delete data
# table = 'students'
# condition = 'age > 20'
#
# sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
#
# db.close()


#query
sql5 = 'SELECT * FROM students WHERE age >= 30'

try:
    cursor.execute(sql5)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')


try:
    cursor.execute(sql5)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')

db.close()