from src.client import todoist_client

def getTaskCompletions(object_id):
    response = todoist_client.getTaskCompletions(object_id)

    # print(response.status_code) // deal with status code errors?

    event_timestamps = []
    for event in response.json()['events']:
        event_timestamps.append(event['event_date'])




