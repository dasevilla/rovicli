import logging
import sys
import os

from cliff.app import App
from cliff.commandmanager import CommandManager
from cliff.lister import Lister


class RoviApp(App):

    log = logging.getLogger(__name__)

    def __init__(self):
        super(RoviApp, self).__init__(
            description='Command line access to the Rovi API',
            version='0.1',
            command_manager=CommandManager('rovicli'),
        )


class RoviCommand(Lister):

    def get_parser(self, prog_name):
        parser = super(RoviCommand, self).get_parser(prog_name)
        parser.add_argument('--api-key', help='Rovi api key',
                            required=False, default=os.getenv('ROVI_API_KEY'))
        parser.add_argument('--api-secret', help='Rovi api secret',
                            required=False, default=os.getenv('ROVI_API_SECRET'))
        return parser


def main(argv=sys.argv[1:]):
    myapp = RoviApp()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
