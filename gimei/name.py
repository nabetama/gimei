# -*- coding: utf-8 -*-
import random


__all__ = ['Name']


class name(object):
    def is_male(self):
        from .gimei import MALE
        return self.gender == MALE

    def is_female(self):
        from .gimei import FEMALE
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

    @classmethod
    def get_all_names(cls):
        from .gimei import Gimei
        return Gimei.NAMES[cls.__name__]


class first_name(name):
    def __init__(self, gender=None):
        from .gimei import GENDER
        from .gimei import Gimei
        self.gender = gender if gender is not None else random.choice(GENDER)
        self.all = random.choice(Gimei.NAMES[self.__class__.__name__][self.gender])


class last_name(name):
    def __init__(self, gender=None):
        from .gimei import GENDER
        from .gimei import Gimei
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
            self.last.kanji,
            self.first.kanji,
        )

    @property
    def hiragana(self):
        return u"{} {}".format(
            self.last.hiragana,
            self.first.hiragana,
        )

    @property
    def katakana(self):
        return u"{} {}".format(
            self.last.katakana,
            self.first.katakana,
        )

    @property
    def is_male(self):
        from .gimei import MALE
        return self.gender == MALE

    @property
    def is_female(self):
        from .gimei import FEMALE
        return self.gender == FEMALE

    def __repr__(self):
        return self.kanji.encode('utf-8')

    @classmethod
    def find_name_by_index(cls, name, idx):
        from .gimei import MALE, FEMALE
        result = []

        token = name.split(' ')
        if len(token) != 2:
            return None
        first_names = first_name.get_all_names()
        last_names = last_name.get_all_names()

        for _names in last_names:
            if _names[idx] == token[0]:
                result.append(_names[idx])
                break

        for _names in first_names[MALE]:
            if _names[idx] == token[1]:
                result.append(token[1])
                break

        if len(result) != 2:
            for _names in first_names[FEMALE]:
                if _names[idx] == token[1]:
                    result.append(token[1])
                    break

        if len(result) == 2:
            return result
        return None

    @classmethod
    def find_name_by_kanji(cls, kanji):
        return cls.find_name_by_index(kanji, 0)

    @classmethod
    def find_name_by_hiragana(cls, hiragana):
        return cls.find_name_by_index(hiragana, 1)

    @classmethod
    def find_name_by_katakana(cls, katakana):
        return cls.find_name_by_index(katakana, 2)
