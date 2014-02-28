#!/usr/bin/env python

from subprocess import Popen, PIPE
import game

def will(expected, actual, assumption):
    if expected != actual:
        raise UserWarning("%s failed: expected '%s', got '%s'" % (assumption, expected, actual))
    print('%s ok' % assumption)

start_output = "You are at start.\nYou can go halfway."

g = game.Game()

# basic walkthrough with an erroneous input
will(start_output, g.start(), 'start output')
will('You cannot go to end', g.do('go to end'), 'unexpected action handling')
will('You go halfway', g.do('go halfway'), 'another place')
will('You go to end', g.do('go to end'), 'expected action')

def command_will(expected, input, assumption):
    game_process = Popen(['./game.py'], stdin=PIPE, stdout=PIPE)
    will(
        expected,
        game_process.communicate(input)[0],
        assumption
    )

command_will(start_output + "\n", '', 'start from command line')

command_will(
    start_output + "\nYou go halfway\nYou go to end\n",
    "go halfway\ngo to end\n",
    'play from command line'
)
