from datetime import datetime, timedelta
bell_schedule = "" # can be REGULAR, CONFERENCE, HOMEROOM
type_of_day = "" # can be A, B
day_of_week = "" #can be MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
days = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
REGULAR = []
CONFERENCE = []
HOMEROOM = []

def get_list_periods(type):
    '''Returns entire list of periods and times given type'''
    day = []
    if type == "REGULAR":
        day = REGULAR
    elif type == "CONFERENCE":
        day = CONFERENCE
    elif type == 'HOMEROOM':
        day = HOMEROOM
    return day

def return_day(num):
    '''Given a num from 0-6 returns Monday-Sunday respectively'''
    return days[num]

def get_current_period(type):
    '''Returns current period(0-num_period) given type of day'''
    current_time = datetime.now()
    current_time = datetime.strptime(str(current_time.hour) + ":" + str(current_time.minute), "%H:%M")
    day = []
    type = type.upper()

    if type == "REGULAR":
        day = REGULAR
    elif type == "CONFERENCE":
        day = CONFERENCE
    elif type == 'HOMEROOM':
        day = HOMEROOM
    
    print("hi")
    print(day)
    if current_time < day[0][0]:
        return -2 # -2 if it is before school

    in_btw_period = 0
    for i in range(len(day)):

        if day[i][0] <= current_time and current_time <= day[i][1]:
            #print(day[i][0], day[i][1], current_time)
            return i
        elif day[i][1] <= current_time:
            in_btw_period = i


    if current_time > day[-1][1]:
        return -3 # -3 if it is after school

    return "-1" + str(in_btw_period) # -1 if it is during the time between periods

def get_current_month():
    '''Returns month string'''
    months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month = datetime.now().month - 1
    return months[month]

def get_current_weekday():
    '''Returns global day_of_week'''
    global day_of_week

    day_of_week = datetime.now().weekday()
    return days[day_of_week].capitalize()

def set_bell_schedule(type):
    '''Sets global bell_schedule'''
    global bell_schedule
    bell_schedule = type.upper()

def get_bell_schedule():
    '''Returns global bell_schedule'''
    return bell_schedule

def set_type_of_day(a_b):
    '''Sets global type_of_day'''
    global type_of_day
    type_of_day = a_b.upper()

def get_type_of_day():
    '''Returns global type_of_day'''
    return type_of_day


def num_periods(num, type):
    '''Sets globals REGULAR, CONFERENCE, HOMEROOM to be of length num'''
    global REGULAR, CONFERENCE, HOMEROOM
    type = type.upper()

    if type == "REGULAR":
        REGULAR = [None for i in range(num)]
    elif type == "CONFERENCE":
        CONFERENCE = [None for i in range(num)]
    elif type == "HOMEROOM":
        HOMEROOM = [None for i in range(num)]

def set_period(period, start_time, end_time, type):
    '''Sets period in globals REGULAR, CONFERENCE, HOMEROOM (based on type) based on start_time, end_time, walking_time'''
    global REGULAR, CONFERENCE, HOMEROOM
    type = type.upper()

    if type == "REGULAR":
        REGULAR[period] = (start_time, end_time)
    elif type == "CONFERENCE":
        CONFERENCE[period] = (start_time, end_time)
    elif type == 'HOMEROOM':
        HOMEROOM[period] = (start_time, end_time)

def set_periods(num_period, start_time, period_length, walking_time):
    '''Sets all the periods given start_time of day (HH:MM), period length (minutes), and walking time (minutes) between periods'''
    time_format = "%H:%M"
    start_time = datetime.strptime(start_time, time_format)
    time_delta_period = timedelta(minutes = period_length)
    time_delta_walk = timedelta(minutes = walking_time)

    if period_length == 40:
        num_period += 1 # Accounts for addition 1 homeroom period
        type = "HOMEROOM"
        num_periods(num_period, type)

        for i in range(num_period):
            if i == 3:
                homeroom_time_delta = timedelta(minutes = 15) # Homeroom is 12 minutes long
                set_period(i, start_time, start_time + homeroom_time_delta, type)
                start_time += homeroom_time_delta + time_delta_walk
                continue
            set_period(i, start_time, start_time + time_delta_period, type)
            start_time += time_delta_period + time_delta_walk

    elif period_length == 37:
        type = "CONFERENCE"
        num_periods(num_period, type)
        time_delta_walk = timedelta(minutes = 4)

        for i in range(num_period):
            set_period(i, start_time, start_time + time_delta_period, type)
            start_time += time_delta_period + time_delta_walk

    else:
        type = "REGULAR"
        num_periods(num_period, type)

        for i in range(num_period):
            set_period(i, start_time, start_time + time_delta_period, type)
            start_time += time_delta_period + time_delta_walk

def get_start_time(period, type):
    type = type.upper()

    if type == "REGULAR":
        return REGULAR[period][0]
    elif type == "CONFERENCE":
        return CONFERENCE[period][0]
    elif type == 'HOMEROOM':
        return HOMEROOM[period][0]

def get_end_time(period, type):
    type = type.upper()

    if type == "REGULAR":
        return REGULAR[period][1]
    elif type == "CONFERENCE":
        return CONFERENCE[period][1]
    elif type == 'HOMEROOM':
        return HOMEROOM[period][1]

def create_stuy_schedule():
    if not (REGULAR or HOMEROOM or CONFERENCE):
        set_periods(10, "8:00", 41, 5) # Sets Stuy Regular Schedule
        set_periods(10, "8:00", 40, 4) # Sets Stuy Homeroom Schedule
        set_periods(10, "8:00", 37, 5) # Sets Stuy Conference Schedule
