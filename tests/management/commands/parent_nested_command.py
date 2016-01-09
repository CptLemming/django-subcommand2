from subcommand.base import SubcommandCommand

from .subcommands.nested import NestedCommand


class Command(SubcommandCommand):
    help = 'My Parent Command'

    subcommands = {
        'nested': NestedCommand,
    }
