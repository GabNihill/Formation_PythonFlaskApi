from typing import Dict, List

import pytest

from people import (
    read_all,
    read_one,
    create,
    delete,
    update,
    get_timestamp,
    PEOPLE)

people_list = [{'fname': 'Kent', 'lname': 'Brockman', 'timestamp': get_timestamp()},
                {'fname': 'Bunny', 'lname': 'Easter', 'timestamp': get_timestamp()},
                {'fname': 'Doug', 'lname': 'Farrell', 'timestamp': get_timestamp()}]


def test_read_all():
    assert read_all() == people_list