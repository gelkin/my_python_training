import re
from random import randrange

from model.contact import Contact


def test_data_contact_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_home = contacts[index]
    contact_edit = app.contact.get_contact_info_from_edit_page(index)
    assert contact_home.firstname.rstrip(" ") == contact_edit.firstname.rstrip(" ")
    assert contact_home.lastname.rstrip(" ") == contact_edit.lastname.rstrip(" ")
    assert contact_home.address.rstrip(" ") == contact_edit.address.rstrip(" ")
    assert contact_home.all_emails_from_home_page == merge_emails_like_on_home_page(contact_edit)
    assert contact_home.all_phones_from_home_page == merge_phones_like_on_home_page(contact_edit)


def test_all_contacts(app, db):
    ui_contacts = app.contact.get_contact_list()
    db_contacts = db.get_contact_list()
    ui_contacts = sorted(ui_contacts, key=Contact.id_or_max)
    db_contacts = sorted(db_contacts, key=Contact.id_or_max)
    for i in range(len(ui_contacts)):
        ui_contact = ui_contacts[i]
        db_contact = db_contacts[i]
        assert remove_doubly_spaces(ui_contact.firstname) == remove_doubly_spaces(db_contact.firstname)
        assert remove_doubly_spaces(ui_contact.lastname) == remove_doubly_spaces(db_contact.lastname)
        assert remove_doubly_spaces(ui_contact.address) == remove_doubly_spaces(db_contact.address)
        assert ui_contact.all_emails_from_home_page == merge_emails_like_on_home_page(db_contact)
        assert ui_contact.all_phones_from_home_page == merge_phones_like_on_home_page(db_contact)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x:x is not None and len(x) > 0,
                                       [contact.email, contact.email2, contact.email3]))

def clear(s):
    return re.sub("[() -]", "", s)

def remove_doubly_spaces(s):
    return " ".join(s.split())

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x:x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


