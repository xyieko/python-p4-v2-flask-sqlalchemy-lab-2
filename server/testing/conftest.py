#!/usr/bin/env python3
import pytest
from app import app, db

@pytest.fixture(autouse=True)
def run_before_tests():
    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()



def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))