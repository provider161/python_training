from models.Group import Group


def test_delete_first_group(app):
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.creation(Group(name="group1", header="skip", footer="skip"))
        app.group.return_to_groups_page()
    app.group.delete_first_group()
    app.group.return_to_groups_page()
    app.open_homepage()