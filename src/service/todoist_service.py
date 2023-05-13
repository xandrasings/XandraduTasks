import json

from src.client import todoist_client
from src.constants.data_constants import *

def updateHabitTaskCompletions():
    habit_task_completions = readHabitTaskCompletions()

    # update
    for habit_id in habit_task_completions:
        for task_id in habit_task_completions[habit_id]:
            habit_task_completions[habit_id][task_id].update(getTaskCompletions(task_id))

    writeHabitTaskCompletions(habit_task_completions)


def readHabitTaskCompletions():
    # deserialize from json file
    with open(FILE_PATH_HABIT_TASK_COMPLETIONS, CODE_READ) as file:
        habit_task_completions = json.load(file)

    # change completion list to set
    for habit_id in habit_task_completions:
        for task_id in habit_task_completions[habit_id]:
            habit_task_completions[habit_id][task_id] = set(habit_task_completions[habit_id][task_id])

    return habit_task_completions


def getTaskCompletions(object_id):
    response = todoist_client.getTaskCompletions(object_id)

    # print(response.status_code) // deal with status code errors?

    event_timestamps = set()
    for event in response.json()['events']:
        event_timestamps.add(event['event_date'])

    return event_timestamps


def writeHabitTaskCompletions(habit_task_completions):
    # serialize to json
    for habit_id in habit_task_completions:
        for task_id in habit_task_completions[habit_id]:
            habit_task_completions[habit_id][task_id] = list(habit_task_completions[habit_id][task_id])
            habit_task_completions[habit_id][task_id].sort(reverse=True)
    jsondata = json.dumps(habit_task_completions, indent=4)

    # save to file
    with open(FILE_PATH_HABIT_TASK_COMPLETIONS, CODE_WRITE) as outfile:
        outfile.write(jsondata)
