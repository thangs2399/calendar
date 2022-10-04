
#################### BASIC DATA STRUCTURE ####################




from datetime import datetime


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
    method() -> type
        description
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
        self.personId = "someID"  # need to change
        self.username = username
        self.email = email
        self.password = password
        self.dob = dob
        self.gender = gender

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
        id : {self.personId}
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
    own : User (class)
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

    def __init__(self, name, user, startTime, endTime, location, description, creationDate):
        self.id = "someId"  # need change
        self.name = name
        self.own = user.getId()   # creator
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


if __name__ == "__main__":

    # testing person class
    name = "Stones"
    email = "stones123@canisius.edu"
    password = "password123"
    dob = datetime(1990, 1, 1)
    gender = "male"

    user1 = User(name, email, password, dob, gender)

    print(user1)
