import datetime


def US03(birthday = datetime.datetime(1900, 1, 1), alive = True, death = "N/A"):
    if not alive:
        if birthday > death:
            return False
        else:
            return True
    else:
        if death != "N/A":
            return False
        return True