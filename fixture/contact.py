import random

from selenium.webdriver.support.select import Select
from model.contact import Contact
import re
from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements(By.XPATH,'//*[@title="Details"]')) > 0):
            wd.find_element(By.LINK_TEXT,"home").click()

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()

    def add_new_contact(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT,"add new").click()

    def fill_data(self,contact):
        wd = self.app.wd
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        # wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        # wd.find_element(By.NAME, "theform").click()
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(contact.homephone)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobilephone)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(contact.workphone)
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(contact.fax)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        if contact.bday!="":
            wd.find_element(By.NAME, "bday").click()
            Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        if contact.bmonth != "":
            wd.find_element(By.NAME, "bmonth").click()
            Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        if contact.byear != "":
            wd.find_element(By.NAME, "byear").click()
            wd.find_element(By.NAME, "byear").clear()
            wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        if contact.aday != "":
            wd.find_element(By.NAME, "aday").click()
            Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        if contact.amonth != "":
            wd.find_element(By.NAME, "amonth").click()
            Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
        if contact.ayear != "":
            wd.find_element(By.NAME, "ayear").click()
            wd.find_element(By.NAME, "ayear").clear()
            wd.find_element(By.NAME, "ayear").send_keys(contact.ayear)
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys(contact.address2)
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys(contact.secondaryphone)
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys(contact.notes)


    def contact_information(self,contact):
        wd = self.app.wd
        self.init_contact_creation()
        self.fill_data(contact)
        self.contact_cache = None
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT,"add new").click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_index(index)
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        alert = wd.switch_to_alert()
        alert.accept()

        self.return_to_home_page()
        self.contact_cache = None


    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_id(id)
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        index = 0
        for row in wd.find_elements(By.NAME, "entry"):
            cell = row.find_elements(By.TAG_NAME, "td")[7]
            s = cell.find_element(By.XPATH, "./a[@href]").get_attribute("href")
            id_number = int(s.split("id=")[1])
            if str(id_number) == id:
                break
            index += 1
        self.select_contact_by_index(index)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def modify_contact_by_index(self,index,contact):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements(By.NAME,"entry")[index]
        cell = row.find_elements(By.TAG_NAME,"td")[7]
        cell.find_element(By.TAG_NAME,"a").click()
        self.fill_data(contact)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, contact):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_id_to_modify(contact.id)
        self.fill_data(contact)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_id_to_modify(self, id):
        wd = self.app.wd
        for row in wd.find_elements(By.NAME, "entry"):
            cell = row.find_elements(By.TAG_NAME, "td")[7]
            s = cell.find_element(By.XPATH, "./a[@href]").get_attribute("href")
            id_number = s.split("id=")[1]
            if id_number == str(id):
                cell.find_element(By.TAG_NAME, "a").click()
                break


    def modify_first_contact(self,contact):
        self.modify_contact_by_index(0,contact)



    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements(By.NAME,"selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd =self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            rows = wd.find_elements(By.XPATH,'//table[@id="maintable"]//tr')
            for element in rows[1:]:
                tds = element.find_elements(By.XPATH,".//child::td")
                s = tds[6].find_element(By.XPATH, "./a[@href]").get_attribute("href")# link with id 'http://localhost/addressbook/view.php?id=27'
                id_number = int(s.split("id=")[1])
                firstname = tds[2].text
                lastname = tds[1].text
                all_phones = tds[5].text
                all_emails = tds[4].text
                address = tds[3].text
                self.contact_cache.append(Contact(firstname=firstname, lastname =lastname , id=id_number,
                                                  all_phones_from_home_page = all_phones, address = address, all_emails_from_home_page=all_emails))

        return list(self.contact_cache)

    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements(By.NAME,"selected[]")[index].click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements(By.NAME,"entry")[index]
        cell = row.find_elements(By.TAG_NAME,"td")[7]
        cell.find_element(By.TAG_NAME,"a").click()

    def open_contact_view_by_index(self,index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements(By.NAME,"entry")[index]
        cell = row.find_elements(By.TAG_NAME,"td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        secondaryphone = wd.find_element(By.NAME, "phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone,
                       address=address,email=email, email2=email2,email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text) .group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def add_contact_to_random_group(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_index(index)
        select = Select(wd.find_element(By.NAME, "to_group"))
        chosen_group = random.choice(select.options)
        chosen_group_id = chosen_group.get_attribute("value")
        select.select_by_value(chosen_group_id)
        wd.find_element(By.XPATH, "//input[@value='Add to']").click()
        self.return_to_home_page()
        return chosen_group_id

    def add_contact_to_group(self, index, group_id):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_index(index)
        select = Select(wd.find_element(By.NAME, "to_group"))
        select.select_by_value(group_id)
        wd.find_element(By.XPATH, "//input[@value='Add to']").click()
        self.return_to_home_page()

    def select_group(self, group_id):
        wd = self.app.wd
        self.return_to_home_page()
        select = Select(wd.find_element(By.NAME, "group"))
        select.select_by_value(group_id)
        self.contact_cache = None

    def select_random_group(self):
        wd = self.app.wd
        self.return_to_home_page()
        select = Select(wd.find_element(By.NAME, "group"))
        chosen_group = random.choice(select.options[2:])
        chosen_group_id = chosen_group.get_attribute("value")
        select.select_by_value(chosen_group_id)
        self.contact_cache = None
        return chosen_group_id

    def delete_contact_from_group(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element(By.XPATH, "//input[@name='remove']").click()
        self.return_to_home_page()
        select = Select(wd.find_element(By.NAME, "group"))
        select.select_by_value("")
        self.contact_cache = None














