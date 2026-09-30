GRACE_PERIOD = 30
FINE_PER_MINUTE = 1.50
MAXIMUM_FINE = 45.00
TICKET_LENGTH = 2 * 60


def time_to_minutes(time_text):
    separator = ':' if ':' in time_text else '.'
    parts = time_text.split(separator)

    if len(parts) != 2 or not all(part.isdigit() for part in parts):
        raise ValueError('Enter a time in the form HH:MM.')

    hours, minutes = (int(part) for part in parts)
    if not 0 <= hours <= 23 or not 0 <= minutes <= 59:
        raise ValueError('Hours must be 00-23 and minutes must be 00-59.')

    return hours * 60 + minutes


def get_time(prompt):
    while True:
        try:
            return time_to_minutes(input(prompt).strip())
        except ValueError as error:
            print(error)


def is_overstayed(minutes_parked):
    return minutes_parked > GRACE_PERIOD


def calculate_fine(minutes_parked, permit_holder):
    if permit_holder or not is_overstayed(minutes_parked):
        return 0.00

    minutes_over = minutes_parked - GRACE_PERIOD
    uncapped_fine = minutes_over * FINE_PER_MINUTE
    return min(uncapped_fine, MAXIMUM_FINE)


def calculate_parking_time(entry_time, exit_time):
    if exit_time < entry_time:
        exit_time += 24 * 60
    return exit_time - entry_time


def format_duration(minutes):
    hours, remaining_minutes = divmod(minutes, 60)
    if hours == 0:
        return f'{remaining_minutes} minute(s)'
    return f'{hours} hour(s) and {remaining_minutes} minute(s)'


def check_parking_session():
    entry_time = get_time('What time did you enter (HH:MM)? ')
    exit_time = get_time('What time did you leave (HH:MM)? ')
    permit_holder = input('Are you a permit holder? (yes/no) ').strip().lower()

    while permit_holder not in ('yes', 'no'):
        permit_holder = input('Please enter yes or no: ').strip().lower()

    minutes_parked = calculate_parking_time(entry_time, exit_time)
    fine = calculate_fine(minutes_parked, permit_holder == 'yes')

    print(f'You parked for {format_duration(minutes_parked)}.')
    if not is_overstayed(minutes_parked):
        print('No fine: you stayed within the 30 minute limit.')
    elif permit_holder == 'yes':
        print('No fine: permit holders are exempt from overstay charges.')
    else:
        minutes_over = minutes_parked - GRACE_PERIOD
        print(f'You overstayed by {minutes_over} minute(s).')
        print(f'Fine: £{fine:.2f}')
        if fine == MAXIMUM_FINE:
            print('The maximum fine has been applied.')


def ticket_book(time_bought, ticket_length=TICKET_LENGTH):
    current_time = get_time('What is the current time (HH:MM)? ')
    time_elapsed = (current_time - time_bought) % (24 * 60)
    time_left = ticket_length - time_elapsed

    if time_left <= 0:
        print('Your ticket has expired!')
    elif time_left <= 30:
        print(f'Your ticket is about to expire. Time left: {format_duration(time_left)}.')
    else:
        print(f'Your ticket is valid. Time left: {format_duration(time_left)}.')

    return (time_bought + ticket_length) % (24 * 60)


check_parking_session()
ticket_time = get_time('What time did you buy your ticket (HH:MM)? ')
ticket_book(ticket_time)