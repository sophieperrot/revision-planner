#!/usr/bin/env python3

"""
Version 1: Command line interface
- basic skeleton of revision planner app layout/pages
- implement basic functionalities
"""
import os
import datetime

from topic import Course, Topic
from utils import read_data, read_log


data_filepath = os.path.join(os.getcwd(), "courses_data.csv")
courses = read_data(data_filepath)

log_filepath = os.path.join(os.getcwd(), "log.csv")
log = read_log(log_filepath, courses) # "date": ["Topic"]

today = datetime.date.today().strftime("%d/%m/%Y")
todays_revision = log[today]


def navigation():
    print("""
(navigation)
1: Today's revision
2: See courses
3: Settings
4: History
    """)
    try:
        next_page = int(input())
    except:
        quit()
    match next_page:
        case 1:
            todays_revision_page()
        case 2:
            courses_page()
        case 3:
            settings_page()
        case 4:
            history_page()
        case _:
            quit()

def home_page():
    print("\nREVISION PLANNER\n----------------")
    navigation()

def todays_revision_page():
    print("\nTODAY'S REVISION\n----------------")
    [print(f" - {topic.name} ({topic.course.name})") for topic in todays_revision]
    navigation()
    
def courses_page():
    print("\nCOURSES PAGE\n------------\n")
    for course in courses.values():
        print(course.name.upper())
        print("-"*len(course.name))
        [print(f" > {topic.name}") for topic in course.topics]
        print()
    if input("add new topic (y/n): ") == "y":
        add_new_topic()
    navigation()

def settings_page():
    print("\nSETTINGS PAGE\n-------------\n")
    print("""- Set daily revision quota
- Change app design
- Account information (potentially)
- Etc.
""")
    if input("add new course (y/n): ") == "y":
        add_new_course()
    navigation()

def history_page():
    print("\nHISTORY PAGE\n------------\n")
    for date, topics in log.items():
        topic_names = [topic.name for topic in topics]
        print(f"{date}\n- {"\n- ".join(topic_names)}\n")
    navigation()

def add_new_topic():
    topic_name = input("topic name: ")
    course_name = input("course name: ")
    try:
        course = courses[course_name]
    except:
        course = Course(course_name)
        
    topic = Topic(topic_name, course)
    course.topics.add(topic)

def add_new_course():
    course_name = input("course name: ")
    course = Course(course_name)
    courses[course.name] = course


home_page()