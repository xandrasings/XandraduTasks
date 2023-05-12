
from client import todoist_client

print("main")
response = todoist_client.getTaskCompletions('832239031')
print(response.status_code)
print(response.json())
print(response.headers)

