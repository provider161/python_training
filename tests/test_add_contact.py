
from models.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_contact_page()
    app.contact.creation(Contact(firstname ='qwer', middlename ='qwer', lastname ='wert', nickname ='asd', title ='fsdf', company ='fsd', address ='dfsdf', home ='df', mobile ='2312', work ='2342', fax ='23213', email ='fsfsd@dfd.ru', email2='sdfsd@dfs.sd', email3 ='efsf@sdfsd.asd', homepage='sfsdfs.sdf', byear ='1900', ayear ='2000', address2 ='sdfsdfsd', phone2='233534', notes ='dfsdf'))
    app.open_homepage()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)