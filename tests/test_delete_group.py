from models.Group import Group
import random


def test_delete_random_group(app, db, check_ui):
    app.group.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.creation(Group(name="group1", header="skip", footer="skip"))
        app.group.return_to_groups_page()
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    app.group.return_to_groups_page()
    #assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    app.open_homepage()