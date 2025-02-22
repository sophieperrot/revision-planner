#!/usr/bin/env python3

import csv
from topic import Course, Topic

def read_data(filepath):
    courses = {}
    with open(filepath) as file:
        contents = csv.DictReader(file)
        for entry in contents:
            course_name = entry["course"]
            topic_name = entry["topic"]
            if course_name not in courses.keys():
                courses[course_name] = Course(course_name)
            course = courses[course_name]
            topic = Topic(topic_name, course)
            if topic not in course.topics:
                course.topics.add(topic)
    return courses

def read_log(filepath, courses):
    log = {}
    with open(filepath) as file:
        contents = csv.DictReader(file)
        for entry in contents:
            date = entry["date"]
            if date not in log.keys():
                log[date] = []
            for t in courses[entry["course"]].topics:
                if t.name == entry["topic"]:
                    topic = t
            log[date].append(topic)
    return log


def schedule_revision():
    pass

