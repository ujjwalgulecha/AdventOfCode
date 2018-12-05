from datetime import datetime

def get_mins(minutes):
    return sum(minutes)

def get_max_minutes(minutes):
    max = -1
    index = -1
    for key, value in minutes.iteritems():
        if value > max:
            max = value
            index = key
    return index

with open("input1.txt") as f:
    data = f.readlines()
    guard_data = {}
    cur_guard = -1
    final_data = {}
    state = None
    for dat in data:
        info = dat.split()
        year = info[0][1:]
        time = info[1]
        time_stamp = year + ' ' + time[:-1]
        final_data[time_stamp] = dat
    for key in sorted(final_data, key=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M')):
        dat = final_data[key]
        info = dat.split()
        time_stamp = info[1]
        word = info[3]
        time = time_stamp.split(":")
        hour = int(time[0])
        minutes = int(time[1][:-1])
        if '#' in word:
            prev_mins = 0
            state = 'up'
            guard = int(word[1:])
            cur_guard = guard
            if cur_guard not in guard_data:
                mins = {}
                for i in range(0,  60):
                    mins[i] = 0
                guard_data[cur_guard] = mins
        else:
            guard_mins = guard_data[cur_guard]
            if state == 'asleep' and word == 'up':
                for i in range(prev_mins, minutes):
                    guard_mins[i]+=1
                state = 'up'
            elif state == 'up' and word == 'asleep':
                state = 'asleep'
            prev_mins = minutes

    max_mins = 0
    id = -1
    val = []
    for key, value in guard_data.iteritems():
        mins = get_mins(value)
        if mins > max_mins:
            max_mins = mins
            id = key
            val = value

    print id * get_max_minutes(val)
