def digitalClock(x):
    hour = x // 3600
    x %= 3600
    minutes = x // 60
    x %= 60
    seconds = x
    print(hour,':',minutes,':',seconds)  
digitalClock(5025)
digitalClock(61201)
digitalClock(87000)