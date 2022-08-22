from sys import maxsize

def remove_doubly_spaces(s):
    return " ".join(s.split())

class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id,self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and\
               remove_doubly_spaces(self.name) == remove_doubly_spaces(other.name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

