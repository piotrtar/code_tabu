import operator
from operator import *
import csv

class Event:

    events = []

    def __init__(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def get_event_name(self):
        return self.__class__.__name__
    
    @classmethod
    def del_event(cls, event):
        cls.events.remove(event)
        

    @classmethod
    def sort_events(cls):
        
        # cls.events = sorted(cls.events, key=operator.attrgetter('date'))

        is_sorted = False

        while not is_sorted and len(cls.events) > 1:
            is_sorted = True

            for i in range(len(cls.events) - 1):
                if cls.events[i].date > cls.events[i+1].date:
                    temp = cls.events[i]
                    cls.events[i] = cls.events[i+1]
                    cls.events[i+1] = temp

                    is_sorted = False


    @classmethod
    def add_event(cls, event):
        cls.events.append(event)
        cls.sort_events()
  

    @classmethod
    def get_events(cls):
        return cls.events


    @staticmethod
    def read_from_csv():
        with open ("Events.csv", 'r') as f:
            reader = csv.reader(f, delimiter = ',')
            for line in reader:
                event_type = line[0]
                date = line[1]
                preffered_mentor = line[2]
                goal = line[3]

                if event_type == "Checkpoint":
                    Checkpoint(date)
                else:
                    PrivateMentoring(date,preffered_mentor,goal)
        

    @staticmethod
    def write_to_csv():
        with open("Events.csv", 'w') as f:
            writer = csv.writer(f, delimiter = ',')
            for event in Event.events:
                if isinstance(event, PrivateMentoring):
                    writer.writerow([event.__class__.__name__,event.date,event.preffered_mentor,event.goal])
                elif isinstance(event, Checkpoint):
                    writer.writerow([event.__class__.__name__,event.date,'',''])


class Checkpoint(Event):

    def __init__(self, date):
        super().__init__(date)

        Event.add_event(self)

    def __str__(self):
        return '{} Checkpoint'.format(self.date)

    @classmethod
    def del_event(cls, event):
        cls.events.remove(event)


class PrivateMentoring(Event):

    def __init__(self, date, preffered_mentor = None, goal = None):
        super().__init__(date)
        self.preffered_mentor = preffered_mentor
        self.goal = goal

        Event.add_event(self)

    def __str__(self):
        return '{} Private mentoring with {} about {}'.format(self.date, self.preffered_mentor, self.goal)
    
    
    @classmethod
    def del_event(cls, event):
        cls.events.remove(event)