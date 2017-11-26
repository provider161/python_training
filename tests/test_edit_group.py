
from models.Group import Group
import random

def test_edit_group_name(app, db, check_ui):
    app.group.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.creation(Group(name="group1", header="skip", footer="skip"))
        app.group.return_to_groups_page()
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = "qqwerty1234"
    index = old_groups.index(group)
    app.group.edit_group_by_id(group.id, group)
    app.group.return_to_groups_page()
    #assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    app.open_homepage()

#def test_edit_group_header(app):
 #   app.group.open_groups_page()
  #  if app.group.count() == 0:
   #     app.group.creation(Group(name="group1", header="skip", footer="skip"))
    #    app.group.return_to_groups_page()
    #old_groups = app.group.get_group_list()
    #app.group.edit_first_group(Group(header ="New header"))
    #app.group.return_to_groups_page()
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
    #app.open_homepage()