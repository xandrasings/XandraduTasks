import requests
import urllib.parse

from src.constants.todoist_constants import *
from src.constants.secrets import *


def getTaskCompletions(object_id):

    params = {
        PARAM_OBJECT_ID: object_id,
        PARAM_OBJECT_TYPE: PARAM_VALUE_ITEM,
        PARAM_EVENT_TYPE: PARAM_VALUE_COMPLETED,
        PARAM_LIMIT: PARAM_VALUE_LIMIT}

    url = DOMAIN + PATH_GET + urllib.parse.urlencode(params)
    headers = {
        HEADER_AUTHORIZATION: HEADER_VALUE_BEARER_PREFIX + TODOIST_BEARER_TOKEN
    }

    return(requests.get(url, headers=headers))
