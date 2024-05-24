from enum import IntEnum, Enum
from typing import List
import datetime
class Priority(IntEnum):
    SEVERE = 1
    SIGNIFICANT = 2
    AFFECTING = 3
    NON_CRITICAL = 4
    ROUTINE = 5

class Status(Enum):
    CREATED = "Created"
    IN_PROGRESS = "In progress"
    TESTING = "Testing"
    CLOSED = "Closed"

class Comment:
    def __init__(self, text: str, user: str, timestamp: datetime):
        self.text = text
        self.user = user
        self.timestamp = timestamp

    #def __str__(self):

class OS(Enum):
    WINDOWS = "Windows"
    MACOS = "MacOS"
    LINUX = "Linux"
    ANDROID = "Android"
    IOS = "iOS"

class Ticket:
    def __init__(self, id: int, description: str, priority: Priority, created_ts: datetime):
        self.id = id
        self.description = description
        self.priority = priority
        self.status = Status.CREATED
        self.created_ts = created_ts
        self.comments = []

    def add_comment(self, text: str, user: str, timestamp: datetime):
        comment = Comment(text, user, timestamp)
        self.comments.append(comment)

    #def __str__(self):

class SoftwareTicket(Ticket):
    def __init__(self, id: int, description: str, priority: Priority, created_ts: datetime, error_message: str, os: List[OS]):
        super().__init__(id, description, priority, created_ts)
        self.error_message = error_message
        self.os = os
    #def __str__(self):

class HardwareTicket(Ticket):
    def __init__(self, id: int, description: str, priority: Priority, component: str, serial_number: str, error_code: str = None):
        super().__init__(id, description, priority, created_ts)
        self.component = component
        self.serial_number = serial_number
        self.error_code = error_code

    #def __str__(self):




