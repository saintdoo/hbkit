# -*- coding: utf-8 -*-
from __future__ import absolute_import
import click
from . import core, random, short


@click.group()
def cli():
    core.setup()


cli.add_command(random.cli, 'random')
cli.add_command(short.cli, 'short')
