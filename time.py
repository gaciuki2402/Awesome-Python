class Time(object):
    def __init__(self,minutes="Time//60",seconds="Time%60"):
        self.minutes=minutes
        self.seconds=seconds
    def TIME(self):
        print(f"{self.minutes}\n{self.seconds}")

class t(Time):

    def __init__(self,minutes,seconds):
        super(). __init__(minutes,seconds)

    def n(self,n):
        print(f"{self.minutes}//60={n}")

    def m(self,m):
        print(f"{self.minutes}%60={m}")
#if_minutes>=60:
T1=t('300','660')
T1.TIME()
#     def r(self,r):
#         print(f"{self.n}//24={r}")
#     def s(self,s):
#         print(f"{self.n}%24={s}")
# if n>=24:


