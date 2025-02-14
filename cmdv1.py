#!/usr/bin/env python3

"""
Version 1: Command line interface
- basic skeleton of revision planner app layout/pages
- implement basic functionalities
"""

from topic import Course, Topic

log = {} # "date": ["Topic"]

# Add courses
stats = Course("statistics")
physics = Course("physics")
chem = Course("chemistry")
maths = Course("maths")

# Add topics to each course
stats_normal = Topic("normal distribution", stats)
stats.topics.add(stats_normal)
physics_waves = Topic("waves", physics)
physics.topics.add(physics_waves)
physics_electricity = Topic("electricity", physics)
physics.topics.add(physics_electricity)
chem_alkenes = Topic("alkenes", chem)
chem.topics.add(chem_alkenes)
maths_circles = Topic("circles", maths)
maths.topics.add(maths_circles)

# Create dictionary of all courses
courses = {}
for course in [stats, physics, chem, maths]:
    courses[course.name] = course

# Harcoding: today's revision
todays_revision = [stats_normal, chem_alkenes, physics_waves]
log["12/02/25"] = todays_revision

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
        print(f"{date}\t{",".join(topic_names)}")
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