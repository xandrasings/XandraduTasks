import requests
import urllib.parse

from src.constants.habitify_constants import *
from src.constants.secrets import *


def get_habits():
    url = DOMAIN + PATH_GET_HABITS
    headers = {
        HEADER_AUTHORIZATION: HABITIFY_TOKEN
    }

    return requests.get(url, headers=headers)


def get_habit_date_status(habit_id, date):
    headers = {
        HEADER_AUTHORIZATION: HABITIFY_TOKEN
    }
    parameters = {
        PARAM_TARGET_DATE: date
    }
    url = f'{DOMAIN}{PATH_GET_STATUS}{habit_id}?{urllib.parse.urlencode(parameters)}'

    return requests.get(url, headers=headers)


def post_habit_log(habit_id, date):
    headers = {
        HEADER_AUTHORIZATION: HABITIFY_TOKEN
    }
    url = f'{DOMAIN}{PATH_POST_LOGS}{habit_id}'
    body = {
        BODY_UNIT_TYPE: BODY_VALUE_REP,
        BODY_VALUE: 1,
        BODY_TARGET_DATE: date
    }

    requests.post(url, json=body, headers=headers)
