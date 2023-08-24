class Base:

    def __init__(self, driver):
        self.driver = driver

    def assert_words(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')