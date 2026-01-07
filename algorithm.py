#!/usr/bin/env python3

from topic import Topic

"""
SM-2 (SuperMemo-2) algorithm, used in Anki
- https://en.wikipedia.org/wiki/SuperMemo#Description_of_SM-2_algorithm
- https://supermemo.guru/wiki/SuperMemo_Guru
- https://web.archive.org/web/20130129115710/http://ankisrs.net/docs/manual.html#what-algorithm 
"""
class SM2Topic(Topic):

    def __init__(self, name, course):
        super().__init__(name, course)
        self.rep_number = 0
        self.easiness_factor = 2.5
        self.interval = 0

def sm2(topic: SM2Topic, user_grade: int):
    if user_grade >= 3:
        if topic.rep_number == 0:
            topic.interval = 1
        elif topic.rep_number == 1:
            topic.interval = 6
        else:
            topic.interval = round(topic.interval * topic.easiness_factor)
        topic.rep_number += 1
    else:
        topic.rep_number = 0
        topic.interval = 1
    topic.easiness_factor += (0.1 - (5 - user_grade) * (0.08 + (5-user_grade) * 0.02))
    if topic.easiness_factor < 1.3: topic.easiness_factor = 1.3