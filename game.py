#!/usr/bin/env python

import sys

places = {
    'start': {
        'go halfway': 'halfway'
    },
    'halfway': {
        'go back': 'start',
        'go to end': None
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
            available_actions = places[self.place].keys()
            if len(available_actions) > 1:
                available_actions[-1] = 'or ' + available_actions[-1]
            action_listing = ", ".join(available_actions)
            return "You are at %s.\nYou can %s." % (self.place, action_listing)
        return "Game over."

if __name__ == '__main__':
    game = Game()
    print(game.start())

    while game.place:
        input = sys.stdin.readline()
        if not input:
            break
        print(game.do(input.strip()))

