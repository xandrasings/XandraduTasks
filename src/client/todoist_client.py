import requests
import urllib.parse

from src.constants.todoist_constants import *
from src.constants.secrets import *


def get_task_completions(object_id):
    headers = {
        HEADER_AUTHORIZATION: f'{HEADER_VALUE_BEARER_PREFIX}{TODOIST_BEARER_TOKEN}'
    }
    parameters = {
        PARAM_OBJECT_ID: object_id,
        PARAM_OBJECT_TYPE: PARAM_VALUE_ITEM,
        PARAM_EVENT_TYPE: PARAM_VALUE_COMPLETED,
        PARAM_LIMIT: PARAM_VALUE_LIMIT_MAX
    }
    url = f'{DOMAIN}{PATH_GET}?{urllib.parse.urlencode(parameters)}'

    return requests.get(url, headers=headers)
