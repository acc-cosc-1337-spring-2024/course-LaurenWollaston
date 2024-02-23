import math

def get_hour(time):
    return((math.floor((time/3600)%24)))
def get_minutes(time):
    return(math.floor(time/60)%60)
def get_seconds(time):
    return(math.floor(time%60))

def standard_time(time):
    return(str(get_hour(time)).zfill(2))+':'+(str(get_minutes(time)).zfill(2))+':'+(str(get_seconds(time)).zfill(2))