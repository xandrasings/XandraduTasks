from service import kamaji_service

kamaji_service.do_stuff()


# import json
# import pytz # $ pip install pytz
#
#
# from datetime import datetime, timezone, timedelta
# from tzlocal import get_localzone
#
# from src.constants.data_constants import *
#
#
#
#
#
# run_timestamp = datetime.now(get_localzone())
# run_timestamp = datetime.now(timezone.utc)
# offset = run_timestamp.utcoffset().total_seconds()
#
# with open(FILE_PATH_HABITIFY_UPDATES, MODE_APPEND) as outfile:
#     outfile.write(f'\n{datetime.now(timezone.utc).strftime(FORMAT_TIMESTAMP)},{get_localzone()}') # TODO
#
# habitify_service.update_habitify()
#
# todoist_service.generate_task_event_list()
#
# home_tz = pytz.timezone("US/Pacific")
# euro_tz = pytz.timezone("Europe/Lisbon")
#
#
#
#
# def aslocaltimestr(utc_dt):
#     return utc_to_local(utc_dt).strftime('%Y-%m-%d %H:%M:%S.%f %Z%z')
#
#
# print(datetime(2023,  1, 1, 0, 0, 0))
# print(aslocaltimestr(datetime(2023,  1, 1, 0, 0, 0, 730000)))
#
# utc_time = datetime(2023,  1, 1, 12, 0, 0)
#
# print(utc_time.strftime('%Y-%m-%d %H:%M:%S.%f %Z%z'))
# print(utc_to_local(utc_time, "US/Pacific"))
# print(utc_to_local(utc_time, "Europe/Lisbon"))
#
#
#
# for i in range(300):
#     print(f'{utc_time + timedelta(days=i)}\t\t{utc_to_local(utc_time + timedelta(days=i), "US/Pacific")}\t\t{utc_to_local(utc_time + timedelta(days=i), "Europe/Lisbon")}')
#
#
#
#
#
#
#
# new_ts =  datetime.now(timezone.utc)
# print(new_ts)
# print(new_ts.strftime('%Z'))
#
# home_tz = pytz.timezone("US/Pacific")
# euro_tz = pytz.timezone("Europe/Lisbon")
#
# print(home_tz.localize(new_ts))
# print(euro_tz.localize(new_ts))
#
# utc_dt = datetime(2023,  1, 1, 0, 0, 0, 730000)
#
# print(home_tz.normalize(utc_dt.replace(tzinfo=pytz.utc).astimezone(home_tz))) # .normalize might be unnecessary
# print(pytz.timezone("Europe/Lisbon").normalize(utc_dt.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Europe/Lisbon")))) # .normalize might be unnecessary
#
