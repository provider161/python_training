from pytest_bdd import scenario
from bdd.contacts_steps import *

@scenario('contacts.feature', 'Add new contact')
def test_add_new_contact():
    pass

@scenario('contacts.feature', 'Delete a contact')
def test_delete_random_contact():
    pass

@scenario('contacts.feature', 'Edit a contact')
def test_edit_contact():
    pass