import random

from model.contact import Contact
from random import randrange
def test_modify_first_contact(app,db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.contact_information(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Petrov", nickname="iv", title="123", company="Petrov", address="Spb", homephone="8123456778", mobilephone="79117685656", workphone="79871234567", fax="123", email="iv@gmail.com", email2="vi@mail.com", email3="bn@mail.com", bday="1" , bmonth = "January", byear = "1980", aday = "9", amonth = "October", ayear = "2000", address2 = "Spb Fontanka", secondaryphone = "11",notes = "11"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="123", middlename="Ivanovich123", lastname="Petrov", nickname="iv", title="123",
                company="Petrov", address="Spb", homephone="8123456778", mobilephone="79117685656", workphone="79871234567", fax="123",
                email="iv@gmail.com", email2="vi@mail.com", email3="bn@mail.com", bday="1", bmonth="January",
                byear="1980", aday="9", amonth="October", ayear="2000", address2="Spb Fontanka", secondaryphone="11",
                notes="11")
    random_contact = random.choice(old_contacts)
    contact.id = random_contact.id
    app.contact.modify_contact_by_id(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    update_contact_by_id(old_contacts, contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max())


def update_contact_by_id(contacts, contact):
    pos = -1
    for i in range(len(contacts)):
        c = contacts[i]
        if c.id == contact.id:
            pos = i
            break
    contacts[pos] = contact