
from models.Group import Group

def test_add_group(app):
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(name ="group1", header ="skip", footer ="skip")
    app.group.creation(group)
    app.group.return_to_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(name ="", header ="", footer ="")
    app.group.creation(group)
    app.group.return_to_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    app.open_homepage()