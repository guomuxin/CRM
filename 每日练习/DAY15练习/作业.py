# 2.写函数：用户输入某年某月，判断这是这一年的第几天（需要用Python的结构化时间）。
# 结构化时间可以通过这样取值：
# import time
# ret = time.localtime()
# print(ret)  # time.struct_time(tm_year=2019, tm_mon=6, tm_mday=28, tm_hour=15, tm_min=50, tm_sec=47, tm_wday=4, tm_yday=179, tm_isdst=0)
# print(ret.tm_year)  # 2019

# info = input("请输入时间 %Y-%m-%d:")
# import time
# year = time.strptime(info,"%Y-%m-%d").tm_year
# info_time = time.mktime(time.strptime(info,"%Y-%m-%d"))
# one_time = time.mktime(time.strptime(f"{year}-01-01","%Y-%m-%d"))
# # days = info_time - one_time
# days = (info_time - one_time)/(24*60*60)+1
# print(f"这是这一年的第{int(days)}天")

# 3.用户输入一个"2019-7-26 20:30:30"和当前时间相比,一共过去了多少年多少月多少天到少小时多少分钟
import time

x = input("请输入2019-7-26 20:30:30:")
time_after = time.time()
time_de = time.localtime( time_after - time.mktime(time.strptime("2019-7-26 20:30:30","%Y-%m-%d %H:%M:%S")))
print(time_de)
print(f"一共过去了{time_de.tm_year-1970}年,{time_de.tm_mon-1}月,{time_de.tm_mday-1}天,{time_de.tm_hour}时,{time_de.tm_min}分")
# 4.写函数，生成一个4位随机验证码（包含数字大小写字母)
count = 0
s = ""
while count < 5:
    r = random.randint(0,122)
    if 0 <= r <= 9:
        s += str(r)
        count += 1
    elif 65 <= r <= 90 or 97 <= r <= 122:
        s += chr(r)
        count += 1
    else:
        continue
print(s)