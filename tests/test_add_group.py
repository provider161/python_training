
from models.Group import Group

def test_add_group(app):
    app.group.open_groups_page()
    app.group.creation(Group(name ="group1", header ="skip", footer ="skip"))
    app.group.return_to_groups_page()

def test_add_empty_group(app):
    app.group.open_groups_page()
    app.group.creation(Group(name ="", header ="", footer =""))
    app.group.return_to_groups_page()
    app.open_homepage()