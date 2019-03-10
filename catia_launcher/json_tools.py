#! /usr/bin/python3.6

import json
import os

json_file = 'config.json'

def create_config():
    """

    Create the config.json file.

    :return: None
    """
    shortcut_path = ''
    json_file = 'config.json'

    while not os.path.isdir(shortcut_path):
        shortcut_path = input('Please enter path to CATIA shortcuts: ')
        if not os.path.isdir(shortcut_path):
            print('Please enter a valid path.')

    json_data = dict()
    json_data['shortcuts_path'] = shortcut_path

    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=4)
