#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:

    def __init__(self, name="", job="Admin"):
        self.name = name
        self.job = job

        if self.job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        elif self.job in APPROVED_JOBS:
            self.job = job

        if self.name == "" or self.name != type(str):
            print("Name must be string between 1 and 25 characters.")
        elif len(self.name) >= 1 and len(self.name) <= 25:
            self.name = name.title()

