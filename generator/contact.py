from models.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt,sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(str(err))  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), address=random_string("address", 10),
            homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10), workphone=random_string("workphone", 10),
            secondaryphone=random_string("secondaryphone", 10), email=random_string("email", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10),
            middlename="", nickname="", title="", company="", fax="", homepage="", byear="", ayear="", address2="", notes="")
            for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))