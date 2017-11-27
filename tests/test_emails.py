from random import randrange
from models.contact import Contact



"""def test_emails_on_homepage(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_editpage = app.contact.get_contact_info_from_editpage(index)
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_editpage)
    app.open_homepage()"""

def test_emails_from_db(app, db):
    contact_emails_from_homepage = app.contact.get_contacts_emails()
    contact_emails_from_db = db.get_contacts_emails()
    for contact in contact_emails_from_db:
        contact.all_emails_from_homepage = merge_emails_like_on_homepage(contact)
    assert sorted(contact_emails_from_homepage, key=Contact.id_or_max) == sorted(contact_emails_from_db, key=Contact.id_or_max)
    app.open_homepage()

def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                    [contact.email, contact.email2, contact.email3])))