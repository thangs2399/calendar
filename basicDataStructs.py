
#################### BASIC DATA STRUCTURE ####################

class Person:
    """
    Person class
    description: class for person

    Attributes
    ----------
    personId : int 
        unique id number for each person
    name : str
        the name of the animal
    email : str
        user's email
    password : str
        user's password
    dob : str
        user's date of birth
    gender : str
        user's gender
    
    Methods
    -------
    method(params)
        short description
    """
    
    def __init__(self, name, email, password, dob, gender) -> None:
        self.personId = "someID"  # need to change
        self.name = name
        self.email = email
        self.password = password
        self.dob = dob
        self.gender = gender


class Event:

    """
    Event class
    description: class for events


    Class Variables
    ---------------
    BEGIN : Date (class)
        no event is allowed to be created before this date
    END : Date (class)
        no event is allowed to be created after this date


    Attributes
    ----------
    eventId : int 
        unique id number for each event
    name : str
        the name of the calendar
    person : Person (class)
        person who created the group
    startTime: Date (class)
        start time of the event
    endTime: Date (class)
        end time of the event    
    location : string
        location of the event
    description : string
        description of the event
    creationDate : Date (class)
        date of when the calendar was

    
    Methods
    -------
    method(params)
        short description
    """

    BEGIN = 2000
    END = 2200

    def __init__(self, name, person, startTime, endTime, location, description, creationDate):
        self.id = "someId"  # need change
        self.name = name
        self.own = person.getName()   # creator
        self.startTime = startTime
        self.endTime = endTime
        self.location = location
        self.description = description
        self.creationDate = creationDate
        

class Schedule:

    """
    Schedule class
    description: class for scheduels

    Attributes
    ----------
    scheduleId : int 
        unique id number for each schedule
    events : dict
        events in the schdule

    
    Methods
    -------
    method(params)
        short description
    """

    def __init__(self, events = {}):
        self.scheduleId = "someId" # need change
        self.events = events


class IndividualCalendar:
    """
    IndividualCalendar class
    description: class for individual calendars

    Attributes
    ----------
    calendarId : int 
        unique id number for each group calendar
    person : Person (class)
        person who created the group
    schedule: Schedule (class)
        user's schedule
    creationDate : Date (class)
        date of when the calendar was

    
    Methods
    -------
    method(params)
        short description
    """
    def __init__(self, person, schedule, creationDate ):
        self.calendarId = "someId" # need to change
        self.own = person.getId()  # creator
        self.schedule = schedule
        self.creationDate = creationDate


class GroupCalendar:
    """
    GroupCalendar class
    description: class for group calendars

    Attributes
    ----------
    calendarId : int 
        unique id number for each group calendar
    name : str
        the name of the calendar
    person : Person (class)
        person who created the group
    schedules: list
        list of each individuals schedule
    members : dict
        members of the group
    creationDate : Date (class)
        date of when the calendar was

    
    Methods
    -------
    method(params)
        short description
    """
    def __init__(self, name, person, schedules, members, creationDate ):
        self.calendarId = "someId" # need to change
        self.name = name
        self.own = person.getId()
        self.schedules = schedules 
        self.members = members
        self.creationDate = creationDate
