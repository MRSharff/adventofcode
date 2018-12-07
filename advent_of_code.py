import os

import requests

try:
    session = os.environ['advent_session_cookie']
except KeyError:
    session = None


class AdventOfCodeException(Exception):
    pass


def get_cached_input(input_file_path):
    with open(input_file_path) as advent_input_file:
        advent_input = advent_input_file.read()
        return advent_input


def write_response(input_path, response):
    os.makedirs(os.path.dirname(input_path), exist_ok=True)
    with open(input_path, 'w') as advent_input:
        advent_input.write(response.text)


def fetch_day_input(day):
    response = requests.get('https://adventofcode.com/2018/day/{}/input'.format(day), cookies={'session': session})
    if not response.ok:
        raise AdventOfCodeException('Could not get day input: bad response code {}'.format(response.status_code))
    return response


def get_day_input(day):
    input_file_path = 'inputs/day{}.txt'.format(day)
    try:
        return get_cached_input(input_file_path).strip()
    except FileNotFoundError:
        if session is None:
            raise AdventOfCodeException('No session defined')
        response = fetch_day_input(day)
        write_response(input_file_path, response)
        return response.text.strip()