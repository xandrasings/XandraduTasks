import json

from src.client import todoist_client
from src.constants.data_constants import *
from src.constants.todoist_constants import *


def get_habit_task_completions():
    habit_task_completions = read_habit_task_completions()
    update_habit_task_completions(habit_task_completions)
    write_habit_task_completions(habit_task_completions)
    return habit_task_completions


def read_habit_task_completions():
    # deserialize from json file
    with open(FILE_PATH_HABIT_TASK_COMPLETIONS, CODE_READ) as file:
        habit_task_completions = json.load(file)

    # change completion list to set
    for habit_id in habit_task_completions:
        for task_id in habit_task_completions[habit_id]:
            habit_task_completions[habit_id][task_id] = set(habit_task_completions[habit_id][task_id])

    return habit_task_completions


def update_habit_task_completions(habit_task_completions):
    for habit_id in habit_task_completions:
        for task_id in habit_task_completions[habit_id]:
            habit_task_completions[habit_id][task_id].update(get_task_completions(task_id))

    return habit_task_completions


def get_task_completions(object_id):
    response = todoist_client.get_task_completions(object_id)

    # TODO deal with unexpected status codes? failures to parse?

    event_timestamps = set()
    for event in response.json()[KEY_EVENTS]:
        event_timestamps.add(event[KEY_EVENT_DATE])

    return event_timestamps


def write_habit_task_completions(habit_task_completions):
    # serialize to json
    for habit_id in habit_task_completions:
        for task_id in habit_task_completions[habit_id]:
            habit_task_completions[habit_id][task_id] = list(habit_task_completions[habit_id][task_id])
            habit_task_completions[habit_id][task_id].sort(reverse=True)
    jsondata = json.dumps(habit_task_completions, indent=4)

    # save to file
    with open(FILE_PATH_HABIT_TASK_COMPLETIONS, CODE_WRITE) as outfile:
        outfile.write(jsondata)
