import pymysql.cursors

# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


try:
    l = db.get_contacts_in_group(Group(id="17"))
    for item in l:
        print(item)
    print(len(l))
    # cursor.execute("select * from addressbook")
    # for row in cursor.fetchall():
    #     print(row)
finally:
    pass
    # connection.close()