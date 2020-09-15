import datetime as dt
import pytz

now_time = input().split()
now_time = [int(i) for i in now_time]
diff = [100, 100, 100]
ans = ''
now_time = now_time[0] * 3600 + now_time[1] * 60 + now_time[2]
for time in pytz.all_timezones:
    check = str(dt.datetime.now(pytz.timezone(time))).split()
    check = check[1][:8]
    check = check.split(":")
    check = [int(i) for i in check]
    check_num = check[0] * 3600 + check[1] * 60 + check[2]
    if abs(check_num - now_time) < diff[0] * 3600 + diff[1] * 60 + diff[2]:
        diff = check
        ans = time
print(ans)