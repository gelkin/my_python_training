from sys import maxsize


def remove_doubly_spaces(s):
    return " ".join(s.split())


class Contact:
    def __init__(self,firstname = "", middlename ="", lastname = "", nickname = "", title = "", company = "", address = "", homephone = "", mobilephone = "", workphone = "", fax = "", email = "", email2 = "", email3 = "", bday = "", bmonth = "", byear = "", aday = "", amonth = "", ayear = "", address2 = "", secondaryphone = "",notes = "", id=None,all_phones_from_home_page =None, all_emails_from_home_page =None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self. title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear =ayear
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id,self.firstname,self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or str(self.id) == str(other.id)) \
               and remove_doubly_spaces(self.firstname) == remove_doubly_spaces(other.firstname)\
               and remove_doubly_spaces(self.lastname) == remove_doubly_spaces(other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
