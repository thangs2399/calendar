
#################### BASIC DATA STRUCTURE ####################



##### IMPORTS #####

from datetime import datetime
# datetime(year, month, day, hour, minute, second, microsecond)



class User:
    """
    Person class
    description: class for person

    Attributes
    ----------
    personId : int 
        unique id number for each person
    username : str
        username
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
    getId() -> int
        get User's ID
    setId(id) -> None
        set Username's ID
    getUserame() -> str
        get Username
    setUsername(username) -> None
        set Username
    getEmail() -> str
        get email
    setEmail(email) -> None
        set email
    getPassword() -> str
        get password
    setPassword(password) -> None
        set password
    getDob() -> Date (class)
        get DOB
    setDob(date) -> None
        set DOB
    getGender() -> str
        get gender
    setGender(gender) -> None
        set gender
    """
    
    def __init__(self, username, email, password, dob, gender) -> None:
        self.id = 1  # need to change
        self.username = username
        self.email = email
        self.password = password
        self.dob = dob
        self.gender = gender

    def getId(self) -> int:
        return self.id

    def setId(self, id) -> None:
        self.id = id

    def getUsername(self) -> str:
        return self.username

    def setUsername(self, username) -> None:
        self.username = username

    def getEmail(self) -> str:
        return self.email

    def setEmail(self, email) -> None:
        self.email = email
    
    def getPassword(self) -> str:
        return self.password

    def setPassword(self, password) -> None:
        self.password = password
    
    def getDob(self) -> datetime:
        return self.dob

    def setDob(self, dob) -> None:
        self.dob = dob
    
    def getGender(self) -> str:
        return self.gender

    def setGender(self, gender) -> None:
        self.gender = gender
    
    # toString
    def __str__(self):
        return f"""
        id : {self.getId()}
        name : {self.getUsername()}
        email : {self.getEmail()}
        password : {self.getPassword()}
        dob : {self.getDob()}
        gender : {self.getGender()}
        """
        

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
    owner : int
        user's id who created the group
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
    getName() -> str
        get event name
    setName(name) -> None
        set event name
    getOwner() -> int
        get owner
    setOwner(owner) -> None
        set owner
    getStartTime() -> datetime
        get event's start time
    setStartTime(startTime) -> None
        set event's start time
    getEndTime() -> datetime
        get event's end time
    setEndTime(endTime) -> None
        set event's end time
    getLocation() -> str
        get event's location
    setLocation(location) -> None
        set event's location
    getDescription() -> str
        get event's description
    setDescription(description) -> None
        set event's description
    getCreationDate() -> datetime
        get event's creation date
    setCreationDate(creationDate) -> None
        set event's creation date
    
    """

    BEGIN = 2000
    END = 2200

    def __init__(self, name, owner, startTime, endTime, location, description, creationDate):
        self.id = "someId"  # need change
        self.name = name
        self.owner = owner.getId()   # creator
        self.startTime = startTime
        self.endTime = endTime
        self.location = location
        self.description = description
        self.creationDate = creationDate
    
    def getName(self) -> str:
        return self.name

    def setName(self, name) -> None:
        self.name = name

    def getOwner(self) -> int:
        return self.owner

    def setOwner(self, owner) -> None:
        self.owner = owner
    
    def getStartTime(self) -> datetime:
        return self.startTime

    def setStartTime(self, startTime) -> None:
        self.startTime = startTime

    def getEndTime(self) -> datetime:
        return self.endTime

    def setEndTime(self, endTime) -> None:
        self.endTime = endTime

    def getLocation(self) -> str:
        return self.location

    def setLocation(self, location) -> None:
        self.location = location
    
    def getDescription(self) -> str:
        return self.description

    def setDescription(self, description) -> None:
        self.description = description
    
    def getCreationDate(self) -> datetime:
        return self.creationDate

    def setCreationDate(self, creationDate) -> None:
        self.creationDate = creationDate

    # toString
    def __str__(self):
        return f"""
        event name : {self.getName()}
        owner : {self.getOwner()}
        start time : {self.getStartTime()}
        end time : {self.getEndTime()}
        location : {self.getLocation()}
        description : {self.getDescription()}
        """


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
    own : User (class)
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
    def __init__(self, user, schedule, creationDate ):
        self.calendarId = "someId" # need to change
        self.own = user.getId()  # creator
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
    own : User (class)
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
    def __init__(self, name, user, schedules, members, creationDate ):
        self.calendarId = "someId" # need to change
        self.name = name
        self.own = user.getId()
        self.schedules = schedules 
        self.members = members
        self.creationDate = creationDate




# TESTING #
if __name__ == "__main__":

    print()
    print()
    print('##### testing Person class ######')
    print()

    name = "Stones"
    email = "stones123@canisius.edu"
    password = "password123"
    dob = (datetime(1990, 1, 20)).strftime("%x")
    gender = "male"

    user1 = User(name, email, password, dob, gender)
    user1.setId(123)

    print(user1)

    print()
    print(30 * '-')

    print()
    print()
    print('##### testing Event class ######')
    print()

    name = "Homework#1"
    owner = user1
    startTime = datetime(2022, 10, 5, 13, 00, 00, 0) # 1pm
    endTime = datetime(2022, 10, 5, 15, 00, 00, 0) # 3pm
    location = "Science Hall"
    description = "do homework"
    creationDate = datetime.now()

    event1 = Event(name, owner, startTime, endTime, location, description, creationDate)

    print(event1)

    print()
    print(30 * '-')
