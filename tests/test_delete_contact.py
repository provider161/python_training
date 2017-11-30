from models.contact import Contact
from models.Group import Group
import random


"""def test_delete_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.open_contact_page()
        app.contact.creation(
            Contact(firstname='qwer', middlename='qwer', lastname='wert', nickname='asd', title='fsdf', company='fsd',
                    address='dfsdf', homephone='45345', mobilephone='2312', workphone='2342', fax='23213', email='fsfsd@dfd.ru',
                    email2='sdfsd@dfs.sd', email3='efsf@sdfsd.asd', homepage='sfsdfs.sdf', byear='1900', ayear='2000',
                    address2='sdfsdfsd', secondaryphone='233534', notes='dfsdf'))
        app.open_homepage()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)
    app.open_homepage()
    #assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)"""

def test_delete_random_contact_from_random_group(app, db, check_ui, orm):
    if len(db.get_group_list()) == 0:
        app.group.open_groups_page()
        app.group.creation(Group(name="group1", header="skip", footer="skip"))
        app.open_homepage()
    group = random.choice(db.get_group_list())
    if len(db.get_contact_list()) == 0:
        app.contact.open_contact_page()
        app.contact.filling_contact_form(
            Contact(firstname='qwer', middlename='qwer', lastname='wert', nickname='asd', title='fsdf', company='fsd',
                    address='dfsdf', homephone='45345', mobilephone='2312', workphone='2342', fax='23213', email='fsfsd@dfd.ru',
                    email2='sdfsd@dfs.sd', email3='efsf@sdfsd.asd', homepage='sfsdfs.sdf', byear='1900', ayear='2000',
                    address2='sdfsdfsd', secondaryphone='233534', notes='dfsdf'))
        app.contact.select_group(group)
        app.contact.submit_contact_creation()
        app.open_homepage()
    old_contacts = orm.get_contacts_in_group(group)
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)
    app.open_homepage()
    #assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = orm.get_contacts_in_group(group)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)