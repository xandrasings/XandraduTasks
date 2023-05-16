import json

from src.client import todoist_client
from src.constants.data_constants import *
from src.constants.todoist_constants import *


def get_task_completions():
    task_completions = read_task_completions()
    update_task_completions(task_completions)
    write_task_completions(task_completions)
    return task_completions


def get_habit_task_completions():
    habit_task_completions = read_habit_task_completions()
    update_habit_task_completions(habit_task_completions)
    write_habit_task_completions(habit_task_completions)
    return habit_task_completions


def read_task_completions():
    # deserialize from json file
    with open(FILE_PATH_TASK_COMPLETIONS, MODE_READ) as file:
        task_completions = json.load(file)

    # change completion list to set
    for task_id in task_completions:
        task_completions[task_id] = set(task_completions[task_id])

    return task_completions


def update_task_completions(task_completions):
    for task_id in task_completions:
        task_completions[task_id].update(get_latest_task_completions(task_id))

    return task_completions


def get_latest_task_completions(object_id):
    response = todoist_client.get_latest_task_completions(object_id)

    # TODO deal with unexpected status codes? failures to parse?

    event_timestamps = set()
    for event in response.json()[KEY_EVENTS]:
        event_timestamps.add(event[KEY_EVENT_DATE])

    return event_timestamps


def write_task_completions(task_completions):
    # serialize to json
    for task_id in task_completions:
        task_completions[task_id] = list(task_completions[task_id])
        task_completions[task_id].sort(reverse=True)
    jsondata = json.dumps(task_completions, indent=4)

    # save to file
    with open(FILE_PATH_TASK_COMPLETIONS, MODE_WRITE) as outfile:
        outfile.write(jsondata)


def read_habit_tasks():
    # deserialize from json file
    with open(FILE_PATH_HABIT_TASKS, MODE_READ) as file:
        return json.load(file)


def read_habit_task_completions():
    # deserialize from json file
    with open(FILE_PATH_HABIT_TASK_COMPLETIONS, MODE_READ) as file:
        habit_task_completions = json.load(file)

    # change completion list to set
    for habit_id in habit_task_completions:
        for task_id in habit_task_completions[habit_id]:
            habit_task_completions[habit_id][task_id] = set(habit_task_completions[habit_id][task_id])

    return habit_task_completions


# def update_task_completions(task_completions):


def update_habit_task_completions(habit_task_completions):
    for habit_id in habit_task_completions:
        for task_id in habit_task_completions[habit_id]:
            habit_task_completions[habit_id][task_id].update(get_task_completions(task_id))

    return habit_task_completions


def write_habit_task_completions(habit_task_completions):
    # serialize to json
    for habit_id in habit_task_completions:
        for task_id in habit_task_completions[habit_id]:
            habit_task_completions[habit_id][task_id] = list(habit_task_completions[habit_id][task_id])
            habit_task_completions[habit_id][task_id].sort(reverse=True)
    jsondata = json.dumps(habit_task_completions, indent=4)

    # save to file
    with open(FILE_PATH_HABIT_TASK_COMPLETIONS, MODE_WRITE) as outfile:
        outfile.write(jsondata)
