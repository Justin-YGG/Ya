# coding: utf-8

from sky.clients import db
from .card import Card

__all__ = ['Card']


def syncdb(destory=False, verbose=True):
    db.engine.echo = bool(verbose)
    if destory:
        db.drop_all()
    db.create_all()
