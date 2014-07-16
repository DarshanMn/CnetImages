import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='neo&trinity',
    db='phone_reviews')
cursor = mydb.cursor()


cursor.execute("select id, name from phone_id;")
result = cursor.fetchall()
for data in result:
	phone_id = data[0]
	phone_name = data[1]
	print str(phone_id) + " " + str(phone_name)


pid = raw_input("Enter phone name: ")

fileName = raw_input("Enter csv file name: ")

csv_data = csv.reader(file(fileName))

for row in csv_data:
    cursor.execute('INSERT INTO phone_images(phone_id, images)''VALUES('+pid+',%s)', row)

mydb.commit()

cursor.close()
print ("Done")
