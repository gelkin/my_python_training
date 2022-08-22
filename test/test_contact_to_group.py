import random
from random import randrange

from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app,db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.contact_information(
            Contact(firstname="Ivan", middlename="Ivanovich", lastname="Petrov", nickname="iv", title="123",
                    company="Petrov", address="Spb", homephone="8123456778", mobilephone="79117685656", workphone="79871234567",
                    fax="123", email="iv@gmail.com", email2="vi@mail.com", email3="bn@mail.com", bday="1",
                    bmonth="January", byear="1980", aday="9", amonth="October", ayear="2000", address2="Spb Fontanka",
                    secondaryphone="11", notes="11"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = db.get_group_list()
    group = random.choice(groups)
    old_contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
    contacts = app.contact.get_contact_list()
    index = -1
    for i in range(len(contacts)):
        c = contacts[i]
        if c not in old_contacts_in_group:
            index = i
            break
    if index == -1:
        app.contact.contact_information(
            Contact(firstname="Ivan", middlename="Ivanovich", lastname="Petrov", nickname="iv", title="123",
                    company="Petrov", address="Spb", homephone="8123456778", mobilephone="79117685656",
                    workphone="79871234567",
                    fax="123", email="iv@gmail.com", email2="vi@mail.com", email3="bn@mail.com", bday="1",
                    bmonth="January", byear="1980", aday="9", amonth="October", ayear="2000", address2="Spb Fontanka",
                    secondaryphone="11", notes="11"))
        index = len(contacts)
        contacts = app.contact.get_contact_list()
    contact_home = contacts[index]
    app.contact.add_contact_to_group(index,group.id)
    new_contacts_in_group = orm.get_contacts_in_group(Group(id=group.id))
    contact_home.id = str(contact_home.id)
    old_contacts_in_group.append(contact_home)
    assert sorted(old_contacts_in_group, key=Group.id_or_max) == sorted(new_contacts_in_group, key=Group.id_or_max)
