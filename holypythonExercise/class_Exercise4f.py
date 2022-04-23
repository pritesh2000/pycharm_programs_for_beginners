class Nobel:
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

    def __str__(self):
        return "{} was the winner of Nobel {} Prize in {}".format(self.winner, self.category, self.year)

np2005 = Nobel("Peace", 2005, "Muhammad Yunus")
print(np2005)
