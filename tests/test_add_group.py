# -*- coding: utf-8 -*-
import pytest

from fixtures.application import Application
from models.Group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_group(app):
    app.open_homepage()
    app.session.login(username = "admin", password = "secret")
    app.open_groups_page()
    app.new_group_creation(Group(name = "group1", header = "skip", footer = "skip"))
    app.return_to_groups_page()
    app.session.logout()

def test_test_add_empty_group(app):
    app.open_homepage()
    app.session.login(username = "admin", password = "secret")
    app.open_groups_page()
    app.new_group_creation(Group(name = "", header = "", footer = ""))
    app.return_to_groups_page()
    app.session.logout()
