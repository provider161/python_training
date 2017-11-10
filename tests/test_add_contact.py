
from models.contact import Contact


def test_add_contact(app):
    contact = Contact(firstname ='qwer', middlename ='qwer', lastname ='wert', nickname ='asd', title ='fsdf',
                      company ='fsd', address ='dfsdf', homephone ='234234', mobilephone ='2312', workphone ='2342',
                      fax ='23213', email ='fsfsd@dfd.ru', email2='sdfsd@dfs.sd', email3 ='efsf@sdfsd.asd',
                      homepage='sfsdfs.sdf', byear ='1900', ayear ='2000', address2 ='sdfsdfsd', secondaryphone='233534', notes ='dfsdf')
    old_contacts = app.contact.get_contact_list()
    app.contact.open_contact_page()
    app.contact.filling_contact_form(contact)
    app.contact.submit_contact_creation()
    app.open_homepage()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)