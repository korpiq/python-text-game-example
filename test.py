#!/usr/bin/env python

from subprocess import Popen, PIPE
import game

def will(expected, actual, assumption):
    if expected != actual:
        raise UserWarning("%s failed: expected '%s', got '%s'" % (assumption, expected, actual))
    print('%s ok' % assumption)

start_output = "You are at start.\nYou can go halfway."
halfway_output = "You go halfway.\nYou are at halfway.\nYou can go to end."
end_output = "You go to end.\nGame over."

g = game.Game()

# basic walkthrough with an erroneous input
will(start_output, g.start(), 'start output')
will('You cannot go to end', g.do('go to end'), 'unexpected action handling')
will(halfway_output, g.do('go halfway'), 'another place')
will(end_output, g.do('go to end'), 'expected action')

def command_will(expected, input, assumption):
    game_process = Popen(['./game.py'], stdin=PIPE, stdout=PIPE)
    will(
        expected,
        game_process.communicate(input)[0],
        assumption
    )

command_will(start_output + "\n", '', 'start from command line')

command_will(
    "\n".join([ start_output, halfway_output, end_output, '' ]),
    "go halfway\ngo to end\n",
    'play from command line'
)
