#!/usr/bin/env python

import game

def will(expected, actual, assumption):
    if expected != actual:
        raise UserWarning("%s: expected '%s', got '%s'" % (assumption, expected, actual))
    print('%s ok' % assumption)

g = game.Game()
will('You are at start', g.start(), 'start output')
will('You cannot act unexpectedly', g.do('act unexpectedly'), 'unexpected action handling')
will('You go to end', g.do('go to end'), 'expected action')

