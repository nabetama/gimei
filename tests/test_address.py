# coding: utf-8
from gimei import Gimei
from gimei import Address

class TestAddress(object):
    def test_kanji_address_in_data(self):
        address = Gimei().address
        assert Address.find_address_by_kanji(address.kanji)

    def test_hiragana_address_in_data(self):
        address = Gimei().address
        assert Address.find_address_by_hiragana(address.hiragana)

    def test_katakana_address_in_data(self):
        address = Gimei().address
        assert Address.find_address_by_katakana(address.katakana)
