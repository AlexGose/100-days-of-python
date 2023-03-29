#!/bin/env python3

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

new_q = Question("1+1=3", "False")
print(new_q)  # temp test code