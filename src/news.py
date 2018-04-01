from shingle import genshingle, canonize, compaire


class News:
    def __init__(self, title, description, url):
        self.title = title
        self.description = description
        self.url = url

    def percentage_of_duplication(self,other):
        cmp1 = genshingle(canonize(self.description))
        cmp2 = genshingle(canonize(other.description))
        return compaire(cmp1, cmp2)

    def __str__(self):
        s = "News '{title}' from url: {url}\n".format(title=self.title, url=self.url)
        # s += "Description: {description}".format(description = self.description)
        return s

    __repr__ = __str__