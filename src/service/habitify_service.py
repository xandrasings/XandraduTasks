import json

from datetime import datetime, timedelta
from tzlocal import get_localzone

from src.client import habitify_client
# from src.constants.data_constants import *
from src.constants.habitify_constants import *
from src.service import todoist_service
from src.dao import dao


def update_habitify():
    habit_behavior = generate_habit_behavior()

    # run_timestamp = datetime.now(get_localzone())
    # offset = run_timestamp.utcoffset().total_seconds()
    #
    # for habit_id in habit_behavior:
    #     for date in habit_behavior[habit_id]:
    #         dt = datetime.strptime(date, FORMAT_DATE)
    #         response = habitify_client.get_habit_date_status(habit_id, dt.strftime(FORMAT_DATE_PARAM))
    #
    #         increment = max(habit_behavior[habit_id][date] - response.json()[KEY_DATA][KEY_PROGRESS][KEY_CURRENT_VALUE],
    #                         0)
    #
    #         # habitify_client.post_habit_log(habit_id, increment, generate_habit_log_date(date, offset))


def generate_habit_behavior():
    task_behavior = todoist_service.get_task_behavior()
    task_habits = dao.get_task_habits()

    habit_behavior = {}

    print(task_behavior)

    for task_id in task_behavior:
        print(task_id)
        habit_id = task_habits[task_id]

        for timestamp in task_behavior[task_id]:
            print(f'{task_id} {timestamp}')
            increment_date = get_increment_date(timestamp, habit_id)

            if increment_date is not None:
                if habit_id not in habit_behavior:
                    habit_behavior[habit_id] = {}
                if increment_date not in habit_behavior[habit_id]:
                    habit_behavior[habit_id][increment_date] = 0

                habit_behavior[habit_id][increment_date] = habit_behavior[habit_id][increment_date] + 1


def get_increment_date(timestamp, habit_id):
    # TODO complex logic about what is the check date for a given habit and timestamp
    return timestamp.strftime(FORMAT_DATE)
