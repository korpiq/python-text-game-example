#!/usr/bin/env python

import subprocess
import game

def will(expected, actual, assumption):
    if expected != actual:
        raise UserWarning("%s failed: expected '%s', got '%s'" % (assumption, expected, actual))
    print('%s ok' % assumption)

g = game.Game()
will('You are at start', g.start(), 'start output')
will('You cannot act unexpectedly', g.do('act unexpectedly'), 'unexpected action handling')
will('You go to end', g.do('go to end'), 'expected action')

will("You are at start\n", subprocess.check_output(['./game.py']), 'start from command line')
