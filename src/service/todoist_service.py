from src.client import todoist_client

def getTaskCompletions(object_id):
    response = todoist_client.getTaskCompletions(object_id)

    # print(response.status_code) // deal with status code errors?

    event_timestamps = set()
    for event in response.json()['events']:
        event_timestamps.add(event['event_date'])

    print(event_timestamps)
    print(type(event_timestamps))

    return event_timestamps




