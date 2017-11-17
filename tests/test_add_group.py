
from models.Group import Group
import pytest
from data.group import constant as testdata

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.creation(group)
    app.group.return_to_groups_page()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    app.open_homepage()