
import pytest
from pytest_mock import mocker
import datetime
from database import (
    create_people,
    select_people_by_lname,
    select_all_peoples,
    update_people,
    delete_people,
    delete_all_people,
    create_connection
)
from flask import (
    make_response,
    abort
)


def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Database direct path for connecting
database = "peoples_db.db"


# Create a handler for our read people (GET)
def read_all():
    conn = create_connection(database)
    with conn:
        rows = select_all_peoples(conn)
        conn.close()
        return rows


def read_one(lname):
    conn = create_connection(database)
    with conn:
        rows = select_people_by_lname(conn, lname)
        conn.close()
        if len(rows) != 0:
            return rows
        else:
            abort(404, 'Person with last name {lname} not found'.format(lname=lname))


def create(person):
    lname = person.get('lname', None)
    fname = person.get('fname', None)

    # Check if person exist in PEOPLE
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            'lname': lname,
            'fname': fname,
            'timestamp': get_timestamp()
        }
        return make_response('{lname} successfully created'.
                             format(lname=lname), 201)

        # If yes, that's an error
    else:
        abort(406, 'person with last name {lname} already exists'
              .format(lname=lname))


def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]['fname'] = person.get('fname')
        PEOPLE[lname]['timestamp'] = get_timestamp()

        return PEOPLE[lname]
    else:
        abort(404, 'Person with this last name {lname} not found'.format(lname=lname))


def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response('{lname} successfully deleted'.format(lname=lname), 200)

    else:
        abort(404, 'Person with this last name {lname} not found'.format(lname=lname))
