class Habit:
    def __init__(self, row):
        self.name = row[0]
        self.id = row[1]
        self.goal = int(row[2])

    def print(self):
        print("HABIT: " + self.name)

