
from models.Group import Group

def test_edit_group_name(app):
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.creation(Group(name="group1", header="skip", footer="skip"))
        app.group.return_to_groups_page()
    app.group.edit_first_group(Group(name = "New group"))
    app.group.return_to_groups_page()

def test_edit_group_header(app):
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.creation(Group(name="group1", header="skip", footer="skip"))
        app.group.return_to_groups_page()
    app.group.edit_first_group(Group(header ="New header"))
    app.group.return_to_groups_page()
    app.open_homepage()