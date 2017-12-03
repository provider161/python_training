from sys import maxsize


class Contact:
    def __init__(self, firstname = None, middlename = None, lastname = None, nickname = None, title = None,
                 company = None, address = None, homephone = None, mobilephone = None, workphone = None,
                 fax = None, email = None, email2 = None, email3 = None, homepage = None, byear = None,
                 ayear = None, address2 = None, secondaryphone = None, notes = None, id = None,
                 all_phones_from_homepage = None, all_emails_from_homepage = None, group= None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.group = group
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.address,
                                                  self.homephone, self.mobilephone, self.workphone, self.secondaryphone,
                                                  self.email, self.email2, self.email3)

    def __eq__(self, other):
        return (self.id == None or other.id == None or self.id == other.id) \
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize