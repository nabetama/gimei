# coding: utf-8
import pytest
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


@pytest.fixture
def address():
    address = Gimei().address
    address.prefecture.prefectures = ['徳島県', 'とくしまけん', 'トクシマケン']
    address.city.cities = ['徳島市', 'とくしまし', 'トクシマシ']
    address.town.towns = ['万代町', 'ばんだいちょう', 'バンダイチョウ']
    return address

def test_str(address):
    assert str(address) == '徳島県徳島市万代町'

def test_repr(address):
    assert repr(address) == "Address(prefecture=['徳島県', 'とくしまけん', 'トクシマケン'], city=['徳島市', 'とくしまし', 'トクシマシ'], town=['万代町', 'ばんだいちょう', 'バンダイチョウ'])"
