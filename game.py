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
            return self.handle_action(action)
        return self.explanation()

    def handle_action(self, action):
        if action in places[self.place]:
            return self.make_action(action)
        return 'You cannot %s' % action 

    def make_action(self, action):
        self.place = places[self.place][action]
        return 'You %s.\n%s' % (action, self.explanation())

    def explanation(self):
        if self.place:
            return self.explanation_for_existing_place()
        return "Game over."

    def explanation_for_existing_place(self):
        return "You are at %s.\nYou can %s." % (
            self.place,
            self.available_action_listing()
        )

    def available_action_listing(self):
        available_actions = places[self.place].keys()
        if len(available_actions) > 1:
            available_actions[-1] = 'or ' + available_actions[-1]
        return ", ".join(available_actions)

def play_a_game(game):
    print(game.start())
    play_until_end(game)

def play_until_end(game):
    while game.place:
        input = sys.stdin.readline()
        if not input:
            break
        print(game.do(input.strip()))

if __name__ == '__main__':
    play_a_game(Game())

