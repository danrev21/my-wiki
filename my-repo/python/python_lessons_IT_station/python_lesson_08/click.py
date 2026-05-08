#!/usr/bin/env python

# используя модуль click, с помощью функций создаем свои команды
# со своими флагами типа --name, --verbose, --version и т.д.
# Если запустить этот скрипт ./main.py или ./ main.py --help
# появится описание его работы, оно формируется из docstring
# внутри скрипта.

import click

@click.group()   # create group (any name)
def cli():
    """Main entry point for the command-line interface."""
    pass

@cli.command()   # create command
def hello():
    """A straightforward program offering a user greeting."""
    click.echo("Hello, user!")

@cli.command()
@click.option('--name', default='user', help='Specify the name for personalized greetings.')
def greet(name):
    """Greet the user with a personalized message."""
    click.echo(f"Hello, {name}!")

@cli.command()
@click.argument('filename', type=click.Path(exists=True))
def read_file(filename):         # при вызове функции read_file как команды вводим read-file (замена _ на -)
    """Read the content of a specified file."""
    with open(filename, 'r') as file:
        content = file.read()
    click.echo(f"File content:\n{content}")

@cli.command()
@click.option('--verbose', is_flag=True, help='Enable verbose mode.')
@click.option('--name', required=True, prompt='Enter your name', help='Specify your name.') # если --name не указано, работает prompt
def greet(verbose, name):
    """A program to greet the user."""
    if verbose:
        click.echo("Running in verbose mode.")
    click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    cli()
