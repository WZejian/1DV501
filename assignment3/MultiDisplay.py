# Create a data class with several methods
from dataclasses import dataclass


@dataclass
class MultiDisplay:
    message: str = None
    count: int = 0

    def set_message(self, s):
        self.message = s

    def set_count(self, n):
        self.count = n

    def to_string(self):
        return f'Message: {self.message}, Count: {self.count}'

    def set_display(self, s, n):
        self.message = s
        self.count = n
        for i in range(self.count):
            print(self.message)

    def display(self):
        for i in range(self.count):
            print(self.message)

    def get_message(self):
        return self.message
