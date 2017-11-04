
from models.Group import Group

def test_edit_group_name(app):
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.creation(Group(name="group1", header="skip", footer="skip"))
        app.group.return_to_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(name = "New group")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    app.group.return_to_groups_page()
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


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