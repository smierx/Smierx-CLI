import datetime
import uuid
import hashlib


def generate_unique_id():
    # UUID4 erzeugen (zufällig)
    unique_id = uuid.uuid4()

    # Hash erstellen und die ersten 8 Zeichen nehmen
    short_id = hashlib.sha256(unique_id.bytes).hexdigest()[:8]

    return short_id.upper()

def get_semester_str(timestamp:str=None):
    if not timestamp:
        timestamp = datetime.date.today()
    else:
        timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%d")

    year = timestamp.year % 100
    month = timestamp.month
    if 4 <= month <= 9:
        return f"{year}_SS"
    else:
        return f"{year}_WS"