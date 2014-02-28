#!/usr/bin/env python

import sys

places = {
    'start': {
        'go halfway': 'halfway'
    },
    'halfway': {
        'go to end': None,
    },
}

class Game:
    def __init__(self):
        self.place = None

    def start(self):
        self.place = 'start'
	return self.explanation()

    def do(self, action):
        if action:
            if action in places[self.place]:
                self.place = places[self.place][action]
	        return 'You %s.\n%s' % (action, self.explanation())
            return 'You cannot %s' % action 
        return self.explanation()

    def explanation(self):
        if self.place:
            available_actions = ", ".join(places[self.place].keys())
            return "You are at %s.\nYou can %s." % (self.place, available_actions)
        return "Game over."

if __name__ == '__main__':
    game = Game()
    output = game.start()

    while output:
        print(output)
        input = sys.stdin.readline()
        if not input:
            break
        output = game.do(input.strip())

