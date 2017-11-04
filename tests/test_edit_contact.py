
from models.contact import Contact


def test_edit_contact(app):
    contact = Contact(firstname='zxc', middlename='zxc', lastname='xczxc', nickname='zxc', title='zc', company='zc',
                      address='sfs', home='fgdff', mobile='34234', work='2342', fax='345345', email='sdf@dfd.ru',
                      email2='sdf@dfs.sd', email3='wewv@sdfsd.asd', homepage='cvdfgdfg.sdf', byear='1950', ayear='2001',
                      address2='wefwefew', phone2='3345345', notes='cdfgc')
    if app.contact.count() == 0:
        app.contact.open_contact_page()
        app.contact.creation(contact)
        app.open_homepage()
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.modify_first()
    app.contact.creation(contact)
    app.open_homepage()
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    new_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)