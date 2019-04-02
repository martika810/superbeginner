class Palindrome:
    def __init__(self, sentence):
        self.sentence = sentence.replace(' ','').lower()

    def compare_character(self, position):
        return self.sentence[position] == self.sentence[-position-1]

    def is_palindrome(self):
        for index in range(int(len(self.sentence)/2)):
            if not self.compare_character(index):
                return False

        return True

sentence1 = Palindrome('My name is Bob')
print(sentence1.is_palindrome()) # False

sentence2 = Palindrome('Nurses run')
print(sentence1.is_palindrome()) # True