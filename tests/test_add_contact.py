# -*- coding: utf-8 -*-
import pytest

from fixtures.application import Application
from models.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        app.open_homepage()
        app.session.login(username = "admin", password = "secret")
        app.contact.open_contact_page()
        app.contact.creation(Contact(firstname ='qwer', middlename ='qwer', lastname ='wert', nickname ='asd', title ='fsdf', company ='fsd', address ='dfsdf', home ='df', mobile ='2312', work ='2342', fax ='23213', email ='fsfsd@dfd.ru', email2='sdfsd@dfs.sd', email3 ='efsf@sdfsd.asd', homepage='sfsdfs.sdf', byear ='1900', ayear ='2000', address2 ='sdfsdfsd', phone2='233534', notes ='dfsdf'))
        app.session.logout()
