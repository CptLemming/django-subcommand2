from subcommand.base import SubcommandCommand

from .sub import MySubcommand


class NestedCommand(SubcommandCommand):
    help = 'Nested'

    subcommands = {
        'sub': MySubcommand,
    }
