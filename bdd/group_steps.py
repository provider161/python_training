from pytest_bdd import given, when, then
from models.Group import Group
import random

@given('a group list')
def group_list(db):
    return db.get_group_list()

@given('a group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.open_groups_page()
    app.group.creation(new_group)
    app.group.return_to_groups_page()

@then('the new group list is equal to the old with added group')
def verify_group_added(db, group_list, new_group, app, check_ui):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    app.open_homepage()


@given('a non empty group list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.open_groups_page()
        app.group.creation(Group(name="group1", header="skip", footer="skip"))
        app.group.return_to_groups_page()
    return db.get_group_list()

@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.open_groups_page()
    app.group.delete_group_by_id(random_group.id)
    app.group.return_to_groups_page()

@then('the new group list is equal to the old list without deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    app.open_homepage()
