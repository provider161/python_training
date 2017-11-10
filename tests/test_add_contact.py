
from models.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), address=random_string("address", 10),
            homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10), workphone=random_string("workphone", 10),
            secondaryphone=random_string("secondaryphone", 10), email=random_string("email", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10),
            middlename="", nickname="", title="", company="", fax="", homepage="", byear="", ayear="", address2="", notes="")
            for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.open_contact_page()
    app.contact.filling_contact_form(contact)
    app.contact.submit_contact_creation()
    app.open_homepage()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)