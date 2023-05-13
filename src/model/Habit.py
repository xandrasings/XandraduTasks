class Habit:
    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.goal = int(row[2])
        self.tasks = []

    def print(self):
        print("HABIT: " + self.name)
