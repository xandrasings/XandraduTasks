import json
import time

from datetime import datetime, timedelta
from src.client import habitify_client
from src.constants.data_constants import *
from src.constants.habitify_constants import *
from src.service import todoist_service


def update_habitify():
    habit_behavior = generate_habit_behavior()

    for habit_id in habit_behavior:
        for date in habit_behavior[habit_id]:
            dt = datetime.strptime(date, FORMAT_DATE)
            response = habitify_client.get_habit_date_status(habit_id, dt.strftime(FORMAT_DATE_PARAM))

            current_val = response.json()[KEY_DATA][KEY_PROGRESS][KEY_CURRENT_VALUE]

            offset = time.localtime().tm_gmtoff

            for i in range(max(habit_behavior[habit_id][date] - current_val, 0)):
                habitify_client.post_habit_log(habit_id, generate_habit_log_date(date, offset))


def generate_habit_behavior():
    task_completions = todoist_service.get_task_completions()
    habit_tasks = read_habit_tasks()

    habit_behavior = {}

    for habit_id in habit_tasks:
        habit_behavior[habit_id] = {}

        for task_id in habit_tasks[habit_id]:
            for completion in task_completions[task_id]:
                completion_day = (
                        datetime.strptime(completion, FORMAT_DATE_TIME_PRECISE) + timedelta(hours=1)).strftime(
                    FORMAT_DATE)
                if completion_day in habit_behavior[habit_id]:
                    habit_behavior[habit_id][completion_day] = habit_behavior[habit_id][completion_day] + 1
                else:
                    habit_behavior[habit_id][completion_day] = 1

    return habit_behavior


def read_habit_tasks():
    # deserialize from json file
    with open(FILE_PATH_HABIT_TASKS, CODE_READ) as file:
        return json.load(file)


def generate_habit_log_date(date, offset):
    return (datetime.strptime(date, FORMAT_DATE) - timedelta(seconds=offset) + timedelta(hours=12)).strftime(
        FORMAT_DATE_TIME_OFFSET)
