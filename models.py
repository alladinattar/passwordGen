
class Password():
    def __init__(self, special=False, digit=False, length=5, up=False):
        self.length = length
        self.up = up
        self.digit = digit
        self.specialChar = special