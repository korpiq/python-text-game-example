#!/usr/bin/env python

import sys

actions = {
    'go to end': 'You go to end',
    'go halfway': 'You go halfway'
}

class Game:
    def start(self):
	return 'You are at start'

    def do(self, action):
        if action in actions:
            return actions[action]
        return 'You cannot act unexpectedly' 

if __name__ == '__main__':
    game = Game()
    output = game.start()

    while output:
        print(output)
        input = sys.stdin.readline().strip()
        if not input:
            break
        output = game.do(input)

