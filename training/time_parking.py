def solution1(E, L):
    entrance_fee = 2
    first_hour_fee = 3
    next_hour_fee = 4

    def to_min(time):
        h,m = time.split(":")
        return int(h)*60 + int(m)

    minutes = to_min(L) - to_min(E)
    hours = -(-minutes //60)

    if hours > 0:
        return 2

    return entrance_fee + first_hour_fee + (hours - 1)*next_hour_fee
 