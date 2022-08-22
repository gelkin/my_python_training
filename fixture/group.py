from model.group import Group
from selenium.webdriver.common.by import By

class GroupHelper:
    def __init__(self, app):
        self.app = app
    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/groups.php") and len(wd.find_elements(By.NAME,"new")) > 0):
            wd.find_element(By.LINK_TEXT,"groups").click()


    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element(By.NAME,"new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element(By.NAME,"submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_filed_value("group_name", group.name)
        self.change_filed_value("group_header", group.header)
        self.change_filed_value("group_footer", group.footer)



    def change_filed_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME,field_name).click()
            wd.find_element(By.NAME,field_name).clear()
            wd.find_element(By.NAME,field_name).send_keys(text)


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT,"groups").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self,index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        #submit deletion
        wd.find_element(By.NAME,"delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element(By.NAME,"delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        self.select_group_by_index(0)


    def select_group_by_index(self,index):
        wd = self.app.wd
        wd.find_elements(By.NAME,"selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0,new_group_data)

    def modify_group_by_index(self,index,new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        #select first group
        self.select_group_by_index(index)
        #open modification form
        wd.find_element(By.NAME,"edit").click()
        #fill group form
        self.fill_group_form(new_group_data)
        #submit modification
        wd.find_element(By.NAME,"update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_group_by_id(self,new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        #select first group
        self.select_group_by_id(new_group_data.id)
        #open modification form
        wd.find_element(By.NAME,"edit").click()
        #fill group form
        self.fill_group_form(new_group_data)
        #submit modification
        wd.find_element(By.NAME,"update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT,"groups").click()



    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(By.NAME,"selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element(By.NAME,"selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)








