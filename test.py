class Palindrome:
    def __init__(self, phrase):
        self.phrase = phrase.replace(' ','').lower()

    def is_position_palindrome(self, index):
        return self.phrase[index] == self.phrase[-index-1]

    def is_palindrome(self):
        for index in range(int(len(self.phrase)/2)):
            if not self.is_position_palindrome(index):
                return False

        return True

palindrome = Palindrome('Nurses run')
print(palindrome.is_palindrome())