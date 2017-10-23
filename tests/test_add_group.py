
from models.Group import Group

def test_add_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.open_groups_page()
    app.group.creation(Group(name ="group1", header ="skip", footer ="skip"))
    app.group.return_to_groups_page()
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.open_groups_page()
    app.group.creation(Group(name ="", header ="", footer =""))
    app.group.return_to_groups_page()
    app.session.logout()
