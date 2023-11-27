import re

class MyString:
    def __init__(self, value="This is the default value."):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, new_value):
        if type(new_value) == str:
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        pass

    new_value = property(get_value, set_value)
