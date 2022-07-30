import pymysql as py
conn=py.connect(host='db1.ckggf7ifzj7k.us-east-1.rds.amazonaws.com',user='admin',password='12345678')
cursor=conn.cursor()
data=cursor.execute("select version()")
print(data)
# cursor.execute("CREATE DATABASE IF NOT EXISTS GIRI")
# cursor.connection.commit()
# cursor.execute("USE  GIRI")

# create_table='''CREATE TABLE IF NOT EXISTS LOGIN (
#                   ID INT not null auto_increment,
#                   USERNAME  TEXT,
#                   PASSWORD TEXT,
#                   primary key(id)
#                 )'''

# cursor.execute(create_table)
# conn.commit()

# insert_table='''INSERT INTO LOGIN (USERNAME,PASSWORD) values ('Giri','12345678')'''

# cursor.execute(insert_table)
# conn.commit()


# view_table='''select * from LOGIN '''
# cursor.execute(view_table)

print(cursor.fetchall())