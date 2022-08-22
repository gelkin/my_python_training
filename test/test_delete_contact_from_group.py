import random
from random import randrange

from model.contact import Contact
from model.group import Group


def test_delete_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.contact_information(
            Contact(firstname="Ivan", middlename="Ivanovich", lastname="Petrov", nickname="iv", title="123",
                    company="Petrov", address="Spb", home="8123456778", mobile="79117685656", work="79871234567",
                    fax="123", email="iv@gmail.com", email2="vi@mail.com", email3="bn@mail.com", bday="1",
                    bmonth="January", byear="1980", aday="9", amonth="October", ayear="2000", address2="Spb Fontanka",
                    phone2="11", notes="11"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = db.get_group_list()
    group = random.choice(groups)
    if len(orm.get_contacts_in_group(Group(id=group.id))) == 0:
        all_contacts = app.contact.get_contact_list()
        index = randrange(len(all_contacts))
        app.contact.add_contact_to_group(index, group.id)
    app.contact.select_group(group.id)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_home = old_contacts[index]
    app.contact.delete_contact_from_group(index)
    new_contacts = orm.get_contacts_in_group(Group(id=group.id))
    contact_home.id = str(contact_home.id)
    new_contacts.append(contact_home)
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)
