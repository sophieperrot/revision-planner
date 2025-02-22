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

def add_new_course(courses):
    course_name = input("course name: ")
    course = Course(course_name)
    courses[course.name] = course

def add_new_topic(filepath, courses):
    topic_name = input("topic name: ")
    course_name = input("course name: ")
    try:
        course = courses[course_name]
    except:
        course = Course(course_name)
    topic = Topic(topic_name, course)
    course.topics.add(topic)
    with open(filepath, "a") as file:
        fieldnames = ["course", "topic", "last revised", "next revise"]
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({"course": course_name, "topic": topic_name, "last revised": None, "next revise": None})

def add_log_entry(filepath, date, topics):
    with open(filepath, "a") as file:
        fieldnames = ["date", "course", "topic"]
        writer = csv.DictWriter(file, fieldnames)
        for topic in topics:
            writer.writerow({"date": date, "course": topic.course.name, "topic": topic.name})

def schedule_revision():
    pass

