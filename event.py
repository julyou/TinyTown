import math
import random

class Event:
    def __lt__(self, other):
        index = random.randint(0, 1)
        if index:
            return self
        return other

    def __init__(self, timestamp, payload, self_parent, other_parent, toxicity):
        self.timestamp = timestamp
        # score will eventually decay with time
        self.score = self.get_raw_score(payload, toxicity)
        # raw score of sentence (does not take time into account)
        self.sent_score = self.score
        self.message = payload
        self.self_parent = self_parent
        self.other_parent = other_parent

    # updates according to exponential decay function
    def update_score(self, curr_time):
        self.score = self.sent_score*math.pow((1-0.05), (curr_time - self.timestamp)/10)
        return self.score
    
    # TODO
    def get_raw_score(self, msg, toxicity):
        if toxicity[msg] == "Benign":
            return random.randint(0, 100)
        return random.randint(0, 100) * -1