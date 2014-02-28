#!/usr/bin/env python

from subprocess import Popen, PIPE
import game

def will(expected, actual, assumption):
    if expected != actual:
        raise UserWarning("%s failed: expected '%s', got '%s'" % (assumption, expected, actual))
    print('%s ok' % assumption)

start_output = "You are at start.\nYou can go halfway."
halfway_output = "You go halfway.\nYou are at halfway.\nYou can go back, or go to end."
end_output = "You go to end.\nGame over."

g = game.Game()

# basic walkthrough with an erroneous input
will(start_output, g.start(), 'start output')
will('You cannot go to end', g.do('go to end'), 'unexpected action handling')
will(halfway_output, g.do('go halfway'), 'another place')
will("You go back.\n" + start_output, g.do('go back'), 'return to start for good measure')
will(halfway_output, g.do('go halfway'), 'go to another place again')
will(end_output, g.do('go to end'), 'expected action')

def command_will(expected, input, assumption):
    game_process = Popen(['./game.py'], stdin=PIPE, stdout=PIPE)
    will(
        expected,
        game_process.communicate(input)[0],
        assumption
    )

command_will(start_output + "\n", '', 'start from command line')

# newline will not exit but reprint situation.
command_will("%s\n%s\n" % (start_output, start_output), "\n", 'start from command line')

# full play through will exit game at end.
command_will(
    "\n".join([ start_output, halfway_output, end_output, '' ]),
    "go halfway\ngo to end\n\n",
    'play from command line'
)
