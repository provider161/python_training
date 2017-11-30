from fixtures.orm import ORMFixture
from models.Group import Group

db = ORMFixture(host='127.0.0.1', port=8889, name='addressbook', user='root', password='root')

try:
    l = db.get_contacts_in_group(Group(id='357'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()