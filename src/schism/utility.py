import datetime
import re

date_pattern = re.compile("@\\d+@")


def unserialize_dates(document):
        
    for key in document:
            value = document[key]
            if value.startswith('@') and date_pattern.match(value):
                timestamp = int(value[1:-1])
                document[key] = datetime.datetime.fromtimestamp(timestamp)

    return document
