from datetime import datetime

def day_formatter(start_time, end_time, lunch_start, lunch_end, total_time):
    width = 24
    l1_l = 'Start Time:'.ljust(width - 4)
    l1_r = start_time.strftime('%H%M')
    l2_l = 'Lunch Start Time:'.ljust(width - 4)
    l2_r = lunch_start.strftime('%H%M')
    l3_l = 'Lunch End Time:'.ljust(width - 4)
    l3_r = lunch_end.strftime('%H%M')
    l4_l = 'End Time:'.ljust(width - 4)
    l4_r = end_time.strftime('%H%M')
    l5_l = 'Total Time:'.ljust(width - 4)
    l5_r = str(total_time)[:-3]

    print()
    print("=" * width)
    print(l1_l + l1_r)
    print(l2_l + l2_r)
    print(l3_l + l3_r)
    print(l4_l + l4_r)
    print()
    print(l5_l + l5_r)
    print("=" * width)
    print()

def calc_time():
    print('Enter all times as four digit 24 hr times without colons (e.g. "1415").')
    start_time = str(input('Enter start time: '))
    lunch_start = str(input('Enter lunch start time: '))
    if lunch_start not in ['n', '']:
        lunch_end = str(input('Enter lunch end time: '))
    else:
        lunch_start = '0000'
        lunch_end = '0000'
    end_time = str(input('Enter end time: '))
    
    times = [start_time, lunch_start, lunch_end, end_time]
    try:
        format_times = [datetime.strptime(time, '%H%M') for time in times]
        total_time = format_times[3] - format_times[0] - (format_times[2] - format_times[1])
        day_formatter(format_times[0], format_times[3], format_times[1], format_times[2], total_time)
    except ValueError:
        print()
        print('Entered time formats are invalid. Please enter times as "HHMM".')
        calc_time()
    input('Press ENTER to exit...')

if __name__ == '__main__':
    calc_time()
