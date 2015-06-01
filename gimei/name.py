# -*- coding: utf-8 -*-

import random
import yaml


class name(object):
    def is_male(self):
        from gimei import MALE
        return self.gender == MALE

    def is_female(self):
        from gimei import FEMALE
        return self.gender == FEMALE

    @property
    def kanji(self):
        return self.all[0]

    @property
    def hiragana(self):
        return self.all[1]

    @property
    def katakana(self):
        return self.all[2]


class first_name(name):
    def __init__(self, gender=None):
        from gimei import GENDER
        from gimei import Gimei
        self.gender = gender if gender is not None else random.choice(GENDER)
        self.all = random.choice(Gimei.NAMES[self.__class__.__name__][self.gender])


class last_name(name):
    def __init__(self, gender=None):
        from gimei import GENDER
        from gimei import Gimei
        self.gender = gender if gender is not None else random.choice(GENDER)
        self.all = random.choice(Gimei.NAMES[self.__class__.__name__])


class Name(object):
    def __init__(self, gender=None):
        if gender is None:
            from gimei import GENDER
            gender = random.choice(GENDER)
        self.gender = gender
        self.first = first_name(self.gender)
        self.last = last_name(self.gender)

    @property
    def kanji(self):
        return u"{} {}".format(
            self.first.kanji,
            self.last.kanji,
        )

    @property
    def hiragana(self):
        return u"{} {}".format(
            self.first.hiragana,
            self.last.hiragana,
        )

    @property
    def katakana(self):
        return u"{} {}".format(
            self.first.katakana,
            self.last.katakana,
        )

    @property
    def is_male(self):
        from gimei import MALE
        return self.gender == MALE

    @property
    def is_female(self):
        from gimei import FEMALE
        return self.gender == FEMALE

    def __repr__(self):
        return self.kanji.encode('utf-8')
