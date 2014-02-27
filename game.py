#!/usr/bin/env python

actions = {
    'go to end': 'You go to end'
}

class Game:
    def start(self):
	return 'You are at start'

    def do(self, action):
        if action in actions:
            return actions[action]
        return 'You cannot act unexpectedly' 

if __name__ == '__main__':
    print(Game().start())

