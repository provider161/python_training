from pytest_bdd import given, when, then
from models.contact import Contact
import random

#Add new contact

@given('a contacts list')
def contacts_list(db):
    return db.get_contact_list()

@given('a contact with <firstname>, <lastname>')
def new_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname, middlename='qwer', nickname='asd', title='fsdf', company='fsd',
                    address='dfsdf', homephone='45345', mobilephone='2312', workphone='2342', fax='23213', email='fsfsd@dfd.ru',
                    email2='sdfsd@dfs.sd', email3='efsf@sdfsd.asd', homepage='sfsdfs.sdf', byear='1900', ayear='2000',
                    address2='sdfsdfsd', secondaryphone='233534', notes='dfsdf')

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.open_contact_page()
    app.contact.filling_contact_form(new_contact)
    app.contact.submit_contact_creation()
    app.open_homepage()

@then('the new contacts list is equal to the old with added contact')
def verify_contact_added(db, contacts_list, new_contact, check_ui, app):
    old_contacts = contacts_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#Delete a contact

@given('a non empty contacts list')
def non_empty_contacts_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.open_contact_page()
        app.contact.creation(
            Contact(firstname='qwer', middlename='qwer', lastname='wert', nickname='asd', title='fsdf', company='fsd',
                    address='dfsdf', homephone='45345', mobilephone='2312', workphone='2342', fax='23213',
                    email='fsfsd@dfd.ru',
                    email2='sdfsd@dfs.sd', email3='efsf@sdfsd.asd', homepage='sfsdfs.sdf', byear='1900', ayear='2000',
                    address2='sdfsdfsd', secondaryphone='233534', notes='dfsdf'))
        app.contact.submit_contact_creation()
        app.open_homepage()
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contacts_list):
    return random.choice(non_empty_contacts_list)

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_by_id(random_contact.id)
    app.open_homepage()

@then('the new contacts list is equal to the old list without deleted contact')
def verify_contact_deleted(non_empty_contacts_list, random_contact, db, app, check_ui):
    old_contacts = non_empty_contacts_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#Edit a contact

@given('a new contact data with <firstname>, <lastname>')
def new_contact_data(firstname, lastname, non_empty_contacts_list):
    new_contact = Contact(firstname=firstname, lastname=lastname, middlename='qwer', nickname='asd', title='fsdf', company='fsd',
            address='dfsdf', homephone='45345', mobilephone='2312', workphone='2342', fax='23213', email='fsfsd@dfd.ru',
            email2='sdfsd@dfs.sd', email3='efsf@sdfsd.asd', homepage='sfsdfs.sdf', byear='1900', ayear='2000',
            address2='sdfsdfsd', secondaryphone='233534', notes='dfsdf')
    contact = random.choice(non_empty_contacts_list)
    new_contact.id = contact.id
    new_contact.index = non_empty_contacts_list.index(contact)
    return new_contact

@when('I edit the random contact from the list with new data')
def edit_contact(new_contact_data, app):
    app.contact.modify_by_id(new_contact_data.id)
    app.contact.filling_contact_form(new_contact_data)
    app.contact.submit_contact_edition()
    app.open_homepage()

@then('the new contacts list is equal to the old list with edited contact')
def verify_contact_edition(db, non_empty_contacts_list, new_contact_data, app, check_ui):
    old_contacts = non_empty_contacts_list
    new_contacts = db.get_contact_list()
    old_contacts[new_contact_data.index] = new_contact_data
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)