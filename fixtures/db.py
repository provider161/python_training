import pymysql.cursors
from models.Group import Group
from models.contact import Contact

class DbFixture():
    def __init__(self, host, name, user, password, port):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.port = port
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, port=port)
        self.connection.autocommit(True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname FROM addressbook WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contacts_phones(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, home , mobile, work, phone2 FROM addressbook WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, home, mobile, work, phone2) = row
                list.append(Contact(id=str(id), homephone=home, mobilephone=mobile, workphone=work, secondaryphone=phone2))
        finally:
            cursor.close()
        return list

    def get_contacts_emails(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, email, email2, email3 FROM addressbook WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, email, email2, email3) = row
                list.append(Contact(id=str(id), email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def get_contacts_names_and_address(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname, address FROM addressbook WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()
