from models.Group import Group
from random import randrange


def test_delete_random_group(app):
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.creation(Group(name="group1", header="skip", footer="skip"))
        app.group.return_to_groups_page()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    app.group.return_to_groups_page()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
    app.open_homepage()