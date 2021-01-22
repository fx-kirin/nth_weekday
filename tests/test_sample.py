#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import datetime
import logging
import os

import kanilog
import pytest
import stdlogging
from add_parent_path import add_parent_path

with add_parent_path():
    import nth_weekday


logger = kanilog.get_module_logger(__file__, 0)


def setup_module(module):
    pass


def teardown_module(module):
    pass


def setup_function(function):
    pass


def teardown_function(function):
    pass


def test_func():
    assert nth_weekday.get_nth_weekday("monday", 2021, 1, 0) == datetime.date(2021, 1, 4)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    kanilog.setup_logger(logfile='/tmp/%s.log' % (os.path.basename(__file__)), level=logging.INFO)
    stdlogging.enable()

    pytest.main([__file__, '-k test_', '-s'])
