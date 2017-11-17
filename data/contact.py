
from models.contact import Contact
import random
import string

constant = [
    Contact(firstname="firstname1", lastname="lastname1", address="address1",
    homephone="homephone1", mobilephone="mobilephone1", workphone="workphone1",
    secondaryphone="secondaryphone1", email="email11", email2="email21", email3="email31",
    middlename="middlename1", nickname="nickname1", title="title1", company="company1", fax="fax1",
    homepage="homepage1", byear="byear1", ayear="ayear1", address2="address21", notes="notes1"),

    Contact(firstname="firstname2", lastname="lastname2", address="address2",
    homephone="homephone2", mobilephone="mobilephone2", workphone="workphone2",
    secondaryphone="secondaryphone2", email="email12", email2="email22", email3="email32",
    middlename="middlename2", nickname="nickname2", title="title2", company="company2", fax="fax2",
    homepage="homepage2", byear="byear2", ayear="ayear2", address2="address22", notes="notes2")
]

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
