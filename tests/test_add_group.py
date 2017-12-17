
from models.Group import Group
import pytest

def test_add_group(app, json_group, db, check_ui):
    group = json_group
    app.group.open_groups_page()
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('When I add the group %s to the list' % group):
        app.group.creation(group)
        app.group.return_to_groups_page()
    with pytest.allure.step('Then the new group list is equal to the old with added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    app.open_homepage()