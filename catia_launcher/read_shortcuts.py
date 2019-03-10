#! /usr/bin/python3.6

import json
import os
import win32com.client

from .json_tools import create_config, json_file

class CATIASettings:

    def __init__(self, env_file):

        self.env_file = "{}.txt".format(env_file)

        self.cat_user_setting_path = None
        self.cat_temp = None
        self.read_env_file()

    def read_env_file(self):

        with open(self.env_file, mode='rt') as file:
            for line in file:
                if line.startswith("CATUserSettingPath"):
                    self.cat_user_setting_path = line.split('=')[1].strip()
                if line.startswith("CATTemp"):
                    self.cat_temp = line.split('=')[1].strip()

        roaming_data = os.getenv("APPDATA")
        local_data = os.getenv("LOCALAPPDATA")

        self.cat_user_setting_path = self.cat_user_setting_path.replace("CSIDL_APPDATA", roaming_data)
        self.cat_temp = self.cat_temp.replace("CSIDL_LOCAL_APPDATA", local_data)

        if not os.path.isdir(self.cat_user_setting_path):
            self.cat_user_setting_path = None
        if not os.path.isdir(self.cat_temp):
            self.cat_temp = None

    def __repr__(self):

        return 'CATIASettings(\n\tenv_file: {}, \n\tcat_user_setting_path: {}, \n\tcat_temp: {})'.format(self.env_file,
                                                                                                         self.cat_user_setting_path,
                                                                                                         self.cat_temp)


class CATIAShortCut:

    def __init__(self, shortcut_link):
        """

        :param str shortcut_link: full path to shortcut.lnk file
        """

        self.shortcut_link = shortcut_link

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(self.shortcut_link)

        self.target_path = shortcut.Targetpath
        self.arguments = shortcut.Arguments

        self.env = None
        self.directory_env = None
        self.split_arguments()
        self.catia_settings = self.get_settings()

    @property
    def is_catia_installed(self):
        return os.path.isfile(self.target_path)

    @property
    def catia_string(self):

        return os.path.splitext(os.path.basename(self.shortcut_link))[0]

    def get_settings(self):

        return CATIASettings(os.path.join(self.directory_env, self.env))

    def split_arguments(self):
        """
        Find the arguments used to launch CATIA. These will probably be used at a later date to find the users
        CATSettings folder so the user can delete all the users settings.
        :return:
        """

        args = self.arguments.split(' ')
        for item, arg in enumerate(args):
            if arg == "-env":
                self.env = args[item + 1]
            if arg == "-direnv":
                self.directory_env = args[item + 1]
                self.directory_env = self.directory_env.strip('"')

    def start_catia(self):
        """
        Method to start CATIA V5. If the shortcut link points to a file that does not exist the method will return
        False otherwise True.

        True does not necessarily mean that CATIA is actually launched successfully.

        :return: Boolean
        """
        if self.is_catia_installed:
            os.startfile(self.shortcut_link)
            return True
        return False

    def __repr__(self):
        return "CATIAShortCut() \n\ttarget_path: {},\n\t arguments :{}".format(self.target_path, self.arguments)


def load_json():

    if not os.path.isfile(json_file):
        print("There doesn't appear to be a config.json file.")
        create_config()
        print("Please restart application.")
        exit()

    with open("config.json") as json_data_file:
        json_data = json.load(json_data_file)

    if not os.path.isdir(json_data['shortcuts_path']):
        raise ValueError('Check shortcuts_path is valid.')

    return json_data


def populate_shortcuts(json_data):
    shortcut_informations = list()
    for root, dirs, files in os.walk(json_data['shortcuts_path']):
        for file in files:
            if os.path.splitext(file)[1] == ".lnk":
                catia_shortcut = CATIAShortCut(os.path.join(root, file))
                shortcut_informations.append(catia_shortcut)

    return shortcut_informations


shortcut_links = populate_shortcuts(load_json())
