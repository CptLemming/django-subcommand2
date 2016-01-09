from django.core.management import call_command, CommandError
from django.test import TestCase
from django.utils.six import StringIO

from .management.commands.parent_nested_command import Command as ParentNestedCommand


class TestSubcommand(TestCase):

    def test_parent_command_throws_exception_if_no_subcommand(self):
        with self.assertRaises(CommandError):
            call_command(
                'parent_command', stdout=StringIO(), interactive=False)

    def test_subcommand_is_callable(self):
        call_command(
            'parent_command', 'sub', stdout=StringIO(), interactive=False)

    def test_nested_parent_throws_exception_with_call_command(self):
        with self.assertRaises(TypeError):
            call_command(
                'parent_nested_command', 'nested', 'sub', stdout=StringIO(), interactive=False)

    def test_nested_parent_is_callable_from_cli(self):
        mock_argv = ['./manage.py', 'parent_nested_command', 'nested', 'sub']
        command = ParentNestedCommand(stdout=StringIO())
        command.requires_system_checks = False
        command.run_from_argv(mock_argv)
