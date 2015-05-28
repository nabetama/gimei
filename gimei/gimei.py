# -*- coding: utf-8 -*-
import yaml


class Gimei(object):
    def __init__(self, gender=None):
        self.name = Name(gender)
        self.address = Address()
