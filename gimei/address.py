# -*- coding: utf-8 -*-

import random


__all__ = ['Address']


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

    @classmethod
    def get_prefectures(cls):
        from gimei import Gimei
        return Gimei.ADDRESSES['addresses']['prefecture']

    @classmethod
    def get_cities(cls):
        from gimei import Gimei
        return Gimei.ADDRESSES['addresses']['city']

    @classmethod
    def get_towns(cls):
        from gimei import Gimei
        return Gimei.ADDRESSES['addresses']['town']

    @classmethod
    def find_address_by_index(cls, a, idx):
        from gimei import Gimei
        if not a:
            return None

        for prefecture in cls.get_prefectures():
            if not a.startswith(prefecture[idx]):
                continue
            for city in cls.get_cities():
                if not a.startswith(prefecture[idx] + city[idx]):
                    continue
                for town in cls.get_towns():
                    if not a.startswith(prefecture[idx] + city[idx] + town[idx]):
                        continue
                    return prefecture[idx] + city[idx] + town[idx]
        return None

    @classmethod
    def find_address_by_kanji(cls, kanji):
        return cls.find_address_by_index(kanji, 0)

    @classmethod
    def find_address_by_hiragana(cls, hiragana):
        return cls.find_address_by_index(hiragana, 1)

    @classmethod
    def find_address_by_katakana(cls, katakana):
        return cls.find_address_by_index(katakana, 2)
