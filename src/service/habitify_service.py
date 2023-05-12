from src.client import habitify_client
from src.dao import habitify_dao

def getHabitifyHabits():
    response = habitify_client.getHabits()

    # print(response.status_code) // deal with status code errors?

    event_timestamps = []
    for event in response.json()['events']:
        event_timestamps.append(event['event_date'])

def getHabits():
    return(habitify_dao.getHabits())


