import json

from src.constants.data_constants import *


def get_data(file_path):
    with open(file_path, MODE_READ) as file:
        return json.load(file)


def update_data(file_path, data):
    # TODO convert to json if necessary

    with open(file_path, MODE_WRITE) as file:
        file.write(json.dumps(data, indent=INDENT))


def get_runtime_logs():
    return get_data(FILE_PATH_RUNTIME_LOGS)  # TODO


def update_runtime_logs(data):
    update_data(FILE_PATH_RUNTIME_LOGS, data)


def get_task_completions():
    return get_data(FILE_PATH_TASK_COMPLETIONS)


def update_task_completions(data):
    update_data(FILE_PATH_TASK_COMPLETIONS, data)


def get_tasks():
    return get_data(FILE_PATH_TASKS)


def get_task_habits():
    return get_data(FILE_PATH_TASK_HABITS)
