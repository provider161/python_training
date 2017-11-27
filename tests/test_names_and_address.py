from random import randrange
from models.contact import Contact


"""def test_names_on_homepage(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_editpage = app.contact.get_contact_info_from_editpage(index)
    assert contact_from_homepage.firstname == contact_from_editpage.firstname
    assert contact_from_homepage.lastname == contact_from_editpage.lastname
    app.open_homepage()

def test_address_on_homepage(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_editpage = app.contact.get_contact_info_from_editpage(index)
    assert contact_from_homepage.address == contact_from_editpage.address
    app.open_homepage()"""

def test_names_and_address_from_db(app, db):
    contacts_names_and_address_from_homepage = app.contact.get_contacts_names_and_address()
    contacts_names_and_address_from_db = db.get_contacts_names_and_address()
    assert sorted(contacts_names_and_address_from_homepage, key=Contact.id_or_max) ==\
           sorted(contacts_names_and_address_from_db, key=Contact.id_or_max)

