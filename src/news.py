from .shingle import genshingle, canonize, compaire


class News:
    def __init__(self, title, description, url):
        self.title = title
        self.description = description
        self.url = url

    def percentage_of_duplication(self, other):
        cmp1 = genshingle(canonize(self.description, "resources/stopWords"))
        cmp2 = genshingle(canonize(other.description, "resources/stopWords"))
        return compaire(cmp1, cmp2)

    def __str__(self):
        s = "Description: '{d}'\n"\
            .format(d=self.description)
        return s

    __repr__ = __str__
