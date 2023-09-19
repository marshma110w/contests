minute_seconds = 60
hour_seconds = 60 * minute_seconds
day_seconds = 24 * hour_seconds
year_seconds = 365 * day_seconds

month_days_count = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def month_days(month):
    return sum(month_days_count[:month])

def to_seconds(timestamp):
    t = timestamp[0] * year_seconds
    t += month_days(timestamp[1]) * day_seconds
    t += timestamp[2] * day_seconds
    t += timestamp[3] * hour_seconds
    t += timestamp[4] * minute_seconds
    t += timestamp[5]
    return t


in1 = tuple(map(int, input().split()))
in2 = tuple(map(int, input().split()))

diff = to_seconds(in2) - to_seconds(in1)

print(diff // day_seconds, diff % day_seconds)

