========
Usage
========

To use django-subcommand in a project::

    # myapp.management.commands.parent_command.py
    from subcommand.base import SubcommandCommand

    from .subcommands.sub import MySubcommand


    class Command(SubcommandCommand):
        help = 'My Parent Command'

        subcommands = {
            'sub': MySubcommand,  # python manage.py parent_command sub
        }


    # myapp.management.commands.subcommands.sub.py
    from django.core.management.base import BaseCommand


    class MySubcommand(BaseCommand):
        help = 'My Sub Command'
