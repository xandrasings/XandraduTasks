import pytz

from datetime import datetime
from src.client import todoist_client

from src.constants.todoist_constants import *
from src.dao import dao


def get_task_behavior():
    task_completions = get_task_completions()
    task_behavior = {}

    for task_id in task_completions:
        task_behavior[task_id] = localize_task_timestamps(list(task_completions[task_id].values()))

    return task_behavior


def get_task_completions():
    task_completions = dao.get_task_completions()

    tasks = dao.get_tasks()

    for task_id in tasks:
        if task_id not in task_completions:
            task_completions[task_id] = {}

        response = todoist_client.get_latest_task_completions(task_id)

        for event in response.json()[KEY_EVENTS]:
            task_completions[task_id][str(event[KEY_ID])] = event[KEY_EVENT_DATE]

    dao.update_task_completions(task_completions)
    return task_completions


def localize_task_timestamps(utc_timestamps):
    localized_timestamps = []

    utc_timestamps.sort(reverse=True)

    for utc_timestamp in utc_timestamps:
        # TODO replace with the magic using local runtimes
        locale = "Europe/Lisbon"
        localized_timestamps.append(localize_timestamp(utc_timestamp, locale))

    return localized_timestamps


def localize_timestamp(timestamp, locale):
    # local time zone conversion
    timestamp = datetime.strptime(timestamp, FORMAT_DATETIME).replace(tzinfo=pytz.utc).astimezone(pytz.timezone(locale))
    # local daylight timeframe conversion
    timestamp = pytz.timezone(locale).normalize(timestamp)

    return timestamp
