import re
from models.contact import Contact
from random import randrange

"""def test_phones_on_homepage(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_editpage = app.contact.get_contact_info_from_editpage(index)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_editpage)
    app.open_homepage()

def test_phones_on_viewpage(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_viewpage = app.contact.get_contact_info_from_viewpage(index)
    app.open_homepage()
    contact_from_editpage = app.contact.get_contact_info_from_editpage(index)
    assert contact_from_viewpage.homephone == contact_from_editpage.homephone
    assert contact_from_viewpage.workphone == contact_from_editpage.workphone
    assert contact_from_viewpage.mobilephone == contact_from_editpage.mobilephone
    assert contact_from_viewpage.secondaryphone == contact_from_editpage.secondaryphone
    app.open_homepage()"""

def test_phones_from_db(app, db):
    contact_phones_from_homepage = app.contact.get_contacts_phones()
    contact_phones_from_db = db.get_contacts_phones()
    for contact in contact_phones_from_db:
        contact.all_phones_from_homepage = merge_phones_like_on_homepage(contact)
    assert sorted(contact_phones_from_homepage, key=Contact.id_or_max) == sorted(contact_phones_from_db, key=Contact.id_or_max)


def clear(field):
    return re.sub("[() -]", "", field)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))