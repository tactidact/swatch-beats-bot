from datetime import datetime
from dateutil import tz


def itime():
    """Calculate and return Swatch Internet Time

    :returns: No. of beats (Swatch Internet Time)
    :rtype: float
    """
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Europe/Zurich')
    time = datetime.utcnow()
    utc_time = time.replace(tzinfo=from_zone)
    zurich_time = utc_time.astimezone(to_zone)

    h, m, s = zurich_time.timetuple()[3:6]

    beats = ((h * 3600) + (m * 60) + s) / 86.4

    if beats > 1000:
        beats -= 1000
    elif beats < 0:
        beats += 1000

    return beats


if __name__ == "__main__":
    print(itime())
