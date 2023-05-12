import csv

from src.model.Habit import Habit

def getHabits():
    file = open('user_data/habits.csv')
    csvreader = csv.reader(file)

    habits = []
    for row in csvreader:
        habits.append(Habit(row))
    return habits