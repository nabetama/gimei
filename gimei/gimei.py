# -*- coding: utf-8 -*-
import yaml


MALE = 'male'
FEMALE = 'female'
GENDER = (MALE, FEMALE)


def yaml_load(file_path, mode='r'):
    f = open(file_path, mode)
    return yaml.load(f)



class Gimei(object):
    NAMES = yaml_load('./data/names.yml')
    ADDRESSES = yaml_load('./data/addresses.yml')
