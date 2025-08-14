from enum import Enum


class AllureSuite(str, Enum):
    AUTHENTICATION = 'Authentication'
    COURSES = 'Courses'
    DASHBOARD = 'Dashboard'