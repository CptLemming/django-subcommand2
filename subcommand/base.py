from django.core.management.base import BaseCommand, CommandError


class SubcommandCommand(BaseCommand):
    """
    Support subcommands in management commands
    """
    subcommands = {}

    def add_arguments(self, parser):
        # Add subcommands to the parser
        subparsers = parser.add_subparsers(
            dest='subcommand',
            title='subcommands',
            description='valid subcommands')
        subparsers.required = True  # Subparser init does not allow setting required...

        for command_name, command_class in self.subcommands.items():
            # Instantiate the command so we can call it's add_arguments method
            command = command_class()

            if len(self.argv):
                # Outputs console friendly errors
                command._called_from_command_line = True

            subparser = subparsers.add_parser(command_name, cmd=command, help=command_class.help)
            command.add_arguments(subparser)

            # In order to display help message output (with all options), copy the actions created
            # by create_parser to the subcommand parser!
            command_parser = command.create_parser(
                self.get_script_from_argv(), self.get_command_name_from_argv())
            subparser._actions = command_parser._actions

    def __init__(self, *args, **kwargs):
        self.argv = []
        super(SubcommandCommand, self).__init__(*args, **kwargs)

    def get_script_from_argv(self):
        try:
            return self.argv[0]
        except IndexError:
            return ''

    def get_command_name_from_argv(self):
        try:
            return self.argv[1]
        except IndexError:
            return self.__class__.__module__.split('.')[-1]

    def run_from_argv(self, argv):
        self.argv = argv  # Store the arguments passed to this command
        return super(SubcommandCommand, self).run_from_argv(argv)

    def get_subcommand_argv(self):
        # Script used to call this Command + remaining command list
        return list([self.get_script_from_argv()] + self.argv[2:])

    def get_command_class(self, options):
        # Use command name from argv over options in order to support nested subcommands
        # TODO: Nested does not support using django.core.management.call_command
        try:
            command_name = self.argv[2]
        except IndexError:
            command_name = options['subcommand']
        return self.subcommands.get(command_name)

    def get_command_class_kwargs(self):
        return {
            'stdout': self.stdout,
            'stderr': self.stderr,
        }

    def handle(self, *args, **options):
        command_class = self.get_command_class(options)
        command_class_kwargs = self.get_command_class_kwargs()
        argv = self.get_subcommand_argv()

        # Call the subcommand
        command = command_class(**command_class_kwargs)
        command.requires_system_checks = False  # Disable checks for subcommands

        if self._called_from_command_line:
            return command.run_from_argv(argv)
        else:
            return command.execute(*args, **options)
