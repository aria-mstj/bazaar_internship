import re
import datetime

f = open("sample.srt", "r")
lines = f.read()


lines = re.findall("(\d{2}):(\d{2}):(\d{2}),(\d{3}) --> (\d{2}):(\d{2}):(\d{2}),(\d{3})", lines)

date = datetime.date(1, 1, 1)
sum = datetime.datetime(1, 1, 1)

for line in lines:
    first = datetime.time(int(line[0]), int(line[1]), int(line[2]), int(line[3]) * 1000)
    second = datetime.time(int(line[4]), int(line[5]), int(line[6]), int(line[7]) * 1000)
    first = datetime.datetime.combine(date, first)
    second = datetime.datetime.combine(date, second)
    second -= first
    sum += second

print(sum)