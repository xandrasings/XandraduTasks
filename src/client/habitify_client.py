import requests
import urllib.parse

from src.constants.habitify_constants import *
from src.constants.secrets import *

def getHabits():


    url = DOMAIN + PATH_GET_HABITS
    headers = {
        HEADER_AUTHORIZATION: HABITIFY_TOKEN
    }

    return(requests.get(url, headers=headers))
