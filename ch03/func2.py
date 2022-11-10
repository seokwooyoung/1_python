"""
# 2 -> 6 / x -> xxx
def triple(x):
    y = x * 3
    return y

print(triple(2))
"""

# 연도 구하기

def today_func(birth):
    from datetime import datetime
    today = datetime.today()
    return today.year - birth + 1

print(today_func(1998))