
from models.contact import Contact
from random import randrange
import random


def test_edit_contact(app, db, check_ui):
    new_contact = Contact(firstname='qqqqqqqqqqqq', middlename='zxc', lastname='xczxc', nickname='zxc', title='zc', company='zc',
                      address='sfs', homephone='4765765', mobilephone='34234', workphone='2342', fax='345345', email='sdf@dfd.ru',
                      email2='sdf@dfs.sd', email3='wewv@sdfsd.asd', homepage='cvdfgdfg.sdf', byear='1950', ayear='2001',
                      address2='wefwefew', secondaryphone='3345345', notes='cdfgc')
    if len(db.get_contact_list()) == 0:
        app.contact.open_contact_page()
        app.contact.filing_contact_form(new_contact)
        app.contact.submit_contact_creation()
        app.open_homepage()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact.id = contact.id
    index = old_contacts.index(contact)
    app.contact.modify_by_id(contact.id)
    app.contact.filling_contact_form(new_contact)
    app.contact.submit_contact_edition()
    app.open_homepage()
    #assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)