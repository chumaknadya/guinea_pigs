from src import News


class Duplication:

    def __init__(self, original, duplication_percentage):
        self.original = original
        self.duplication_percentage = duplication_percentage

    def __str__(self):
        s = "duplicates " + self.original.title + \
            " with " + str(self.duplication_percentage) + " percentage"
        return s

    __repr__ = __str__
