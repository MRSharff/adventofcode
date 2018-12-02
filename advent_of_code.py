import os

import requests

session = os.environ['advent_session_cookie']


class AdventOfCodeException(Exception):
    pass


def get_day_input(day):
    response = requests.get('https://adventofcode.com/2018/day/{}/input'.format(day), cookies={'session': session})
    if not response.ok:
        raise AdventOfCodeException('Could not get day input: bad response code {}'.format(response.status_code))
    return response.text
