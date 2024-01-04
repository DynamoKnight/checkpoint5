# Write your solution here!
class EdPost:
    '''
    Represents a question on a question board
    '''
    def __init__(self, title, tag='General', comments=None):
        self._title = title
        self._tag = tag
        self._comments = [] if comments is None else comments

    def __repr__(self):
        print(self._title)

    def get_title(self):
        return self._title

    def get_tag(self):
        return self._tag

    def add_comment(self, comment):
        self._comments.append(comment)

    def display(self):
        print(f'{self._title} ({self._tag})')
        print('Comments:')
        for comment in self._comments:
            print(' ', comment)
    