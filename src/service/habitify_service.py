import json

from datetime import datetime, timedelta
from tzlocal import get_localzone

from src.client import habitify_client
# from src.constants.data_constants import *
from src.constants.habitify_constants import *
from src.service import todoist_service
from src.dao import dao


def update_habitify():
    habit_history = generate_habit_history()
    # print(habit_behavior)


def generate_habit_behavior():
    task_behavior = todoist_service.get_task_behavior()
    task_habits = dao.get_task_habits()

    habit_behavior = {}

    for task_id in task_behavior:
        habit_id = task_habits[task_id]

        for timestamp in task_behavior[task_id]:
            increment_date = get_increment_date(timestamp, habit_id)

            if increment_date is not None:
                if habit_id not in habit_behavior:
                    habit_behavior[habit_id] = {}
                if increment_date not in habit_behavior[habit_id]:
                    habit_behavior[habit_id][increment_date] = 0

                habit_behavior[habit_id][increment_date] = habit_behavior[habit_id][increment_date] + 1

    return habit_behavior


def get_increment_date(timestamp, habit_id):
    # TODO complex logic about what is the check date for a given habit and timestamp
    return timestamp.strftime(FORMAT_DATE)

def generate_habit_history():
    habit_behavior = generate_habit_behavior()
    habits = dao.get_habits()
