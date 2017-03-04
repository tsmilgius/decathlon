def to_seconds(time):
    """ accepts time result as string in (min.sec.msec) and returns time result as string in (sec.msec)"""
    tl = time.split('.')
    ti = int(tl[0])*60 + int(tl[1])
    return  str(ti) + '.'+ tl[2]
