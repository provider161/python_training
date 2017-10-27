class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def creation(self, Group):
        wd = self.app.wd
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(Group)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def fill_group_form(self, Group):
        self.change_field_value("group_name", Group.name)
        self.change_field_value("group_header", Group.header)
        self.change_field_value("group_footer", Group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        self.select_first_group()
        # open edition form
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit group edition
        wd.find_element_by_name("update").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self ):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))