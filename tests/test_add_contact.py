
from models.contact import Contact

def test_add_contact(app, data_contact, db, check_ui):
    contact = data_contact
    old_contacts = db.get_contact_list()
    app.contact.open_contact_page()
    app.contact.filling_contact_form(contact)
    app.contact.submit_contact_creation()
    app.open_homepage()
    #assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)