from subcommand.base import SubcommandCommand

from .subcommands.sub import MySubcommand


class Command(SubcommandCommand):
    help = 'My Parent Command'

    subcommands = {
        'sub': MySubcommand,
    }
