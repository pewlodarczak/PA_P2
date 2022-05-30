class Navigation():

    def __init__(self):
        self.history = []
        self.pos = 0

    def addUrl(self, url):
        self.history.append(url)
        self.pos += 1

    def goBack(self):
        # print(self.history[len(self.history)-2])
        #return self.history[len(self.history)-2]
        prevUrl = ''
        if (self.pos < 2):
            return 'Empty history'
        else:
            # print(self.history[self.pos-2])
            prevUrl = self.history[self.pos-2]
            self.pos -= 1
            return prevUrl

    def __repr__(self) -> str:
        return " -> ".join(self.history)


if __name__ == '__main__':
    nav = Navigation()
    nav.addUrl('slashdot.org')
    nav.addUrl('google.com')
    nav.addUrl('yahoo.com')
    print(nav)
    print(nav.goBack())
    print(nav.goBack())
    print(nav.goBack())
