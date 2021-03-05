import selenium
import json


class Reporter:
    def __init__(self):
        with open("secret.json",'r') as file:
            self.data = json.load(file)

    def login(self):
        return NotImplementedError

    def register_hours(self):
        return NotImplementedError

    def submit(self):
        return NotImplementedError

    # TODO pendiente diseñar logout.