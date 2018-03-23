import datetime
import pytz


def datetime_helper(time):
    """Get UTC timestamp from API, convert it to local for storage."""
    # utcdt = weather_json['dt']  # returns epoch integer
    # convert api epoch to datetime string using datetime.datetime
    new = datetime.datetime.fromtimestamp(time).strftime('%H:%M %d/%m/%Y')
    datetime_object = datetime.datetime.strptime(new, '%H:%M %d/%m/%Y')

    local_tz = pytz.timezone('Australia/Perth')
    local_time = datetime_object.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_time
