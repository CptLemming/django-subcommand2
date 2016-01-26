==================
django-subcommand2
==================

.. image:: https://travis-ci.org/CptLemming/django-subcommand2.png?branch=master
    :target: https://travis-ci.org/CptLemming/django-subcommand2


Documentation
-------------

The full documentation is at https://django-subcommand2.readthedocs.org.

Install
-------

Install django-subcommand::

    pip install django-subcommand2

Usage
-----

::

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
