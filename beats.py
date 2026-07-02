from datetime import datetime, timedelta, timezone


def itime(now=None):
    """Calculate and return Swatch Internet Time

    :returns: No. of beats (Swatch Internet Time)
    :rtype: float
    """
    if now is None:
        now = datetime.now(timezone.utc)
    elif now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    else:
        now = now.astimezone(timezone.utc)

    bmt = now + timedelta(hours=1)
    h, m, s = bmt.timetuple()[3:6]

    beats = ((h * 3600) + (m * 60) + s) / 86.4

    return beats % 1000


if __name__ == "__main__":
    print(itime())
