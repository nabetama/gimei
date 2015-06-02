# -*- coding: utf-8 -*-

import random
import yaml


class Prefecture(object):
    def __init__(self):
        from gimei import Gimei
        self.prefectures = random.choice(Gimei.ADDRESSES['addresses']['prefecture'])

    @property
    def kanji(self):
        return u"{}".format(
            self.prefectures[0]
        )

    @property
    def hiragana(self):
        return u"{}".format(
            self.prefectures[1]
        )

    @property
    def katakana(self):
        return u"{}".format(
            self.prefectures[2]
        )


class City(object):
    def __init__(self):
        from gimei import Gimei
        self.cities = random.choice(Gimei.ADDRESSES['addresses']['city'])

    @property
    def kanji(self):
        return u"{}".format(
            self.cities[0]
        )

    @property
    def hiragana(self):
        return u"{}".format(
            self.cities[1]
        )

    @property
    def katakana(self):
        return u"{}".format(
            self.cities[2]
        )


class Town(object):
    def __init__(self):
        from gimei import Gimei
        self.towns = random.choice(Gimei.ADDRESSES['addresses']['town'])

    @property
    def kanji(self):
        return u"{}".format(
            self.towns[0]
        )

    @property
    def hiragana(self):
        return u"{}".format(
            self.towns[1]
        )

    @property
    def katakana(self):
        return u"{}".format(
            self.towns[2]
        )


class Address(object):
    def __init__(self):
        self.prefecture = Prefecture()
        self.city = City()
        self.town = Town()

    @property
    def kanji(self):
        return u"{}{}{}".format(
            self.prefecture.kanji,
            self.city.kanji,
            self.town.kanji,
        )

    @property
    def hiragana(self):
        return u"{}{}{}".format(
            self.prefecture.hiragana,
            self.city.hiragana,
            self.town.hiragana,
        )

    @property
    def katakana(self):
        return u"{}{}{}".format(
            self.prefecture.katakana,
            self.city.katakana,
            self.town.katakana,
        )

    def __repr__(self):
        return self.kanji.encode('utf-8')
