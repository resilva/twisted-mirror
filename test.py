#!/usr/bin/python
""" Test file of the Mirror twisted client.
"""


from twisted.internet import reactor
from mirror import MirrorClient


def on_mirror(tag, state):
    """ Print message when a tag is installed or removed from the mirror.
    """
    state_text = 'On' if state is True else 'Off'
    print '[RFID] [Mirror] {0} is now {1}'.format(tag, state_text)

if __name__ == '__main__':
    # pylint: disable=C0103
    mirror = MirrorClient('/dev/mirror')
    mirror.subscribe(on_mirror)
    reactor.callWhenRunning(mirror.start)
    reactor.run()
