#!/usr/bin/env python

import sys

places = {
    'start': {
        'go halfway': 'halfway'
    },
    'halfway': {
        'go to end': 'end',
    },
    'end': None
}

class Game:
    def __init__(self):
        self.place = None

    def start(self):
        self.place = 'start'
	return 'You are at start'

    def do(self, action):
        if action in places[self.place]:
            self.place = places[self.place][action]
	    return 'You %s' % action
        return 'You cannot %s' % action 

if __name__ == '__main__':
    game = Game()
    output = game.start()

    while output:
        print(output)
        input = sys.stdin.readline().strip()
        if not input:
            break
        output = game.do(input)

