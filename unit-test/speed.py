from random import randint


def get_speed():
    dt = randint(40, 120)
    print(dt)
    return dt


def is_speed_violation():
    speed = get_speed()
    if speed < 60 or speed > 100:
        return True
    return False