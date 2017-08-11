from view import *
from datetime import *
from model import *

def start():

    main_menu()
    choice = get_choice()
    while choice != "0":
        if choice == "1":
            book_private_mentoring()
        elif choice == "2":
            book_checkpoint()
        elif choice == "3":
            show_all_events()
        elif choice == "4":
            reschedule_event()
        elif choice == "5":
            cancel_event()
        main_menu()
        choice = get_choice()

def get_date(provide_date):
    while True:
        date_input = provide_date()
        try:
            dt = datetime.strptime(date_input, '%Y-%m-%d')
            return str(date(dt.year, dt.month, dt.day))
            
        except ValueError:
            wrong_input()

def mentor_choice_validation():
    while True:
        try:
            mentor = int(provide_mentor())
            if 0 < mentor < 6:
                return mentor
        except (ValueError, TypeError):
            pass

def get_mentor():
    print_mentor_list()
    mentor = mentor_choice_validation()
    
    if mentor == 1:
        chosen_mentor = mentors[1]
    elif mentor == 2:
        chosen_mentor = mentors[2]
    elif mentor == 3:
        chosen_mentor = mentors[3]
    elif mentor == 4:
        chosen_mentor = mentors[3]
    elif mentor == 5:
        chosen_mentor = mentors[3]
    
    return chosen_mentor

def book_private_mentoring():
    date = get_date(provide_date)
    private_mentor = get_mentor()
    subject = get_goal()
    PrivateMentoring(date,private_mentor,subject)

def book_checkpoint():
    date = get_date(provide_date)
    Checkpoint(date)

def show_all_events():
    print_all_events(Event.events)

def event_choice_validation():
    while True:
        try:
            event_choice = int(provide_event_number())
            if 0 < event_choice < 3:
                return event_choice
        except (ValueError, TypeError):
            pass

def get_event_name():
    print_events_list()
    event_choice = event_choice_validation()
    
    if event_choice == 1:
        chosen_event = events[1]
    elif event_choice == 2:
        chosen_event = events[2]
    
    return chosen_event

def collect_events_same_date():

    events_with_the_same_date = []
    given_date = get_date(provide_date_to_reschedule)

    for event in Event.events:
        if event.date == given_date:
            events_with_the_same_date.append(event)

    return events_with_the_same_date

def search_date_to_reschedule(same_date_events_list):

    new_date = get_date(provide_new_date)
    event_name = get_event_name()
    for event in same_date_events_list:
        if event_name == event.get_event_name():
            event.date = new_date
            return event.date
    return None

def reschedule_event():
    same_date_events_list = collect_events_same_date()
    if search_date_to_reschedule(same_date_events_list) is None:
        wrong_date_or_event()
    else:
        success_reschedule_msg()

def search_date_to_remove(same_date_events_list):
    event_name = get_event_name()
    for event in same_date_events_list:
        if event_name == event.get_event_name():
            if event_name == events[1]:
                Event.del_event(event)
                return event
            else:
                Event.del_event(event)
                return event
    return None

def cancel_event():
    same_date_events_list = collect_events_same_date()
    if search_date_to_remove(same_date_events_list) is None:
        wrong_date_or_event()
    else:
        success_deletion_msg()    