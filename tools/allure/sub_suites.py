from enum import Enum


class AllureSubSuite(str, Enum):
    AUTHORIZATION = 'Authorization'
    COURSES = 'Courses'
    DASHBOARD = 'Dashboard'
    REGISTRATION = 'Registration'