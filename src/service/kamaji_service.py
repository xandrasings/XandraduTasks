from datetime import datetime
from tzlocal import get_localzone

from src.constants.data_constants import *
from src.dao import dao
from src.service import habitify_service


def do_stuff():
    establish_runtime()
    habitify_service.update_habitify()


def establish_runtime():
    runtime = datetime.utcnow().strftime(FORMAT_TIMESTAMP)
    timezone = str(get_localzone())
    update_logs(runtime, timezone)
    return runtime


def update_logs(runtime, timezone):
    runtime_logs = dao.get_runtime_logs()
    runtime_logs[runtime] = timezone
    dao.update_runtime_logs(runtime_logs)