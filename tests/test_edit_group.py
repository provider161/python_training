
from models.Group import Group

def test_edit_first_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.open_groups_page()
    app.group.edit_first_group(Group(name ="zxcvv", header ="zxcxzczx", footer ="zxczxc"))
    app.group.return_to_groups_page()
    app.open_homepage()
    app.session.logout()