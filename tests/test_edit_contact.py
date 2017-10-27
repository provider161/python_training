
from models.contact import Contact


def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.open_contact_page()
        app.contact.creation(
            Contact(firstname='qwer', middlename='qwer', lastname='wert', nickname='asd', title='fsdf', company='fsd',
                    address='dfsdf', home='df', mobile='2312', work='2342', fax='23213', email='fsfsd@dfd.ru',
                    email2='sdfsd@dfs.sd', email3='efsf@sdfsd.asd', homepage='sfsdfs.sdf', byear='1900', ayear='2000',
                    address2='sdfsdfsd', phone2='233534', notes='dfsdf'))
    app.contact.modify_first()
    app.contact.creation(Contact(firstname ='zxc', middlename ='zxc', lastname ='xczxc', nickname ='zxc', title ='zc', company ='zc', address ='sfs', home ='fgdff', mobile ='34234', work ='2342', fax ='345345', email ='sdf@dfd.ru', email2='sdf@dfs.sd', email3 ='wewv@sdfsd.asd', homepage='cvdfgdfg.sdf', byear ='1950', ayear ='2001', address2 ='wefwefew', phone2='3345345', notes ='cdfgc'))