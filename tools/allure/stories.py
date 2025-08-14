from enum import Enum


class AllureStory(str, Enum):
    AUTHORIZATION = 'Authorization'
    COURSES = 'Courses'
    DASHBOARD = 'Dashboard'
    REGISTRATION = 'Registration'