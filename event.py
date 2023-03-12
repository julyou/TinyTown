import math

class Event:
    def __init__(self, timestamp, sent_score, payload, self_parent, other_parent):
        self.timestamp = timestamp
        # score will eventually decay with time
        self.score = sent_score
        # raw score of sentence (does not take time into account)
        self.sent_score = sent_score
        self.message = payload
        self.self_parent = self_parent
        self.other_parent = other_parent

    # updates according to exponential decay function
    def update_score(self, curr_time):
        self.score = self.sent_score*math.pow((1-0.05), (curr_time - self.timestamp)/10)
        return self.score