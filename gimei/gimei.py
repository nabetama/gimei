# -*- coding: utf-8 -*-
import random
import yaml


from address import Address
from name import Name

MALE = 'male'
FEMALE = 'female'
GENDER = (MALE, FEMALE)


def yaml_load(file_path, mode='r'):
    f = open(file_path, mode)
    return yaml.load(f)



class Gimei(object):
    NAMES = yaml_load('./data/names.yml')
    ADDRESSES = yaml_load('./data/addresses.yml')

    def __init__(self, gender=None):
        if gender is None:
            gender = random.choice(GENDER)
        self.gender = gender


    @property
    def name(self):
        return Name(self.gender)

    @property
    def address(self):
        return Address()
