

mentors = {1:"Mateusz Ostafi",
                2:"Agnieszka Koszany",
                3:"Dominik Starzyk",
                4:"Mateusz Steliga",
                5:"Marcin Izworski"}

events = {1:"PrivateMentoring",
                2:"Checkpoint"}


def main_menu():
    print("""
    Choose option:
    1. Book Private Mentoring
    2. Book checkpoint
    3. Show all my events
    4. Reschedule event
    5. Cancel Event
    0. Exit program
    """)

def print_mentor_list():
    print("""
    Choose mentor:
        1. Mateusz Ostafi
        2. Agnieszka Koszany
        3. Dominik Starzyk
        4. Mateusz Steliga
        5. Marcin Izworski
        """)

def print_events_list():
    print("""
    Choose event:
        1. PrivateMentoring
        2. Checkpoint
        """)

def provide_mentor():
    return input("What mentor is preffered for private mentoring?: ")

def get_choice():
    return input("Enter option from the menu: ")

def provide_date():
    return input('Type date in format YYYY-MM-DD: ')

def provide_date_to_reschedule():
    return input('Type the date you want to change or delete in format YYYY-MM-DD: ')

def provide_new_date():
    return input('Type new date in format YYYY-MM-DD: ')

def date_for_reschedule_event():
    return input('Enter the date of the event you want to reschedule: ')

def new_date_for_reschedule_event():
    return input('Enter new date for the event you want to reschedule: ')

def wrong_input():
    print("Incorrect format")

def get_goal():
    return input("What is the goal of the private mentoring lesson?: ")

def print_all_events(events):
    for event in events:
        print(event)

def wrong_date_or_event():
    print("There is no such date or event at this time")

def success_reschedule_msg():
    print("Event rescheduled successfully")

def success_deletion_msg():
    print("Event deleted successfully")

def provide_event_number():
    return input("What event do you want to change?: ")

def provide_event_number_to_delete():
    return input("What event do you want to delete?: ")
    