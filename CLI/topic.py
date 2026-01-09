#!/usr/bin/env python3

class Course:

    def __init__(self, name):
        self.name = name
        self.topics = set()

class Topic:

    def __init__(self, name, course, mastery = None):
        self.name = name
        self.course = course
        self.last_revised = None
        self.next_revise = None
        self.mastery = mastery