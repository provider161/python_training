
from models.contact import Contact


def test_add_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.modify_first()
    app.contact.creation(Contact(firstname ='zxc', middlename ='zxc', lastname ='xczxc', nickname ='zxc', title ='zc', company ='zc', address ='sfs', home ='fgdff', mobile ='34234', work ='2342', fax ='345345', email ='sdf@dfd.ru', email2='sdf@dfs.sd', email3 ='wewv@sdfsd.asd', homepage='cvdfgdfg.sdf', byear ='1950', ayear ='2001', address2 ='wefwefew', phone2='3345345', notes ='cdfgc'))
    app.session.logout()