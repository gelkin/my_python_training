import random

from model.group import Group
from random import randrange

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    r_group = random.choice(old_groups)
    group = Group(name="New group")
    group.id = r_group.id
    app.group.modify_group_by_id(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    update_group_by_id(old_groups, group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key= Group.id_or_max)

def update_group_by_id(groups, group):
    pos = -1
    for i in range(len(groups)):
        g = groups[i]
        if g.id == group.id:
            pos = i
            break
    groups[pos] = group

#def test_modify_group_header(app):
    #old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header="New header"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
