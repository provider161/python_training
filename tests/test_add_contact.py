from models.contact import Contact
from models.Group import Group
import random

"""def test_add_contact(app, data_contact, db, check_ui):
    contact = data_contact
    old_contacts = db.get_contact_list()
    app.contact.open_contact_page()
    app.contact.filling_contact_form(contact)
    app.contact.submit_contact_creation()
    app.open_homepage()
    #assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)"""

"""def test_add_contact_to_random_group(app, data_contact, db, check_ui, orm):
    contact = data_contact
    if len(db.get_group_list()) == 0:
        app.group.open_groups_page()
        app.group.creation(Group(name="group1", header="skip", footer="skip"))
        app.open_homepage()
    group = random.choice(db.get_group_list())
    old_contacts = orm.get_contacts_in_group(group)
    app.contact.open_contact_page()
    app.contact.filling_contact_form(contact)
    app.contact.select_group(group)
    app.contact.submit_contact_creation()
    app.open_homepage()
    #assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = orm.get_contacts_in_group(group)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)"""

def test_move_contact_to_random_group(app, db, check_ui, orm):
    if len(db.get_group_list()) == 0:
        app.group.open_groups_page()
        app.group.creation(Group(name="group1", header="skip", footer="skip"))
        app.open_homepage()
    if len(db.get_contact_list()) == 0:
        app.contact.open_contact_page()
        app.contact.filling_contact_form(
            Contact(firstname='qwer', middlename='qwer', lastname='wert', nickname='asd', title='fsdf', company='fsd',
                    address='dfsdf', homephone='45345', mobilephone='2312', workphone='2342', fax='23213', email='fsfsd@dfd.ru',
                    email2='sdfsd@dfs.sd', email3='efsf@sdfsd.asd', homepage='sfsdfs.sdf', byear='1900', ayear='2000',
                    address2='sdfsdfsd', secondaryphone='233534', notes='dfsdf'))
        app.contact.submit_contact_creation()
        app.open_homepage()
    if len(db.get_contacts_in_groups()) == len(db.get_contact_list()):
        app.group.open_groups_page()
        app.group.creation(Group(name="group1", header="skip", footer="skip"))
        app.open_homepage()
    group = random.choice(db.get_group_list())
    contact = random.choice(db.get_contact_list())
    old_contacts = orm.get_contacts_in_group(group)
    app.contact.select_by_id(contact)
    app.contact.move_to_group_by_group_id(group)
    app.open_homepage()
    #assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = orm.get_contacts_in_group(group)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)