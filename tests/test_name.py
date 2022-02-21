# coding: utf-8
import pytest
from gimei import Gimei
from gimei import Name


class TestName(object):
    def test_kanji_name_in_data(self):
        name = Gimei().name
        assert Name.find_name_by_kanji(name.kanji)

    def test_hiragana_name_in_data(self):
        name = Gimei().name
        assert Name.find_name_by_hiragana(name.hiragana)

    def test_katakana_name_in_data(self):
        name = Gimei().name
        assert Name.find_name_by_katakana(name.katakana)

    def test_romaji_name_in_data(self):
        name = Gimei().name
        assert Name.find_name_by_romaji(name.romaji)

    def test_create_name_from_gender(self):
        name = Gimei('male').name
        assert name.is_male

    def test_create_name_from_gender(self):
        name = Gimei('female').name
        assert name.is_female

@pytest.fixture
def name():
    name = Gimei().name
    name.gender    = 'female'
    name.first.all = ['七祐', 'なゆ', 'ナユ', 'Nayu']
    name.last.all  = ['佐野', 'さの', 'サノ', 'Sano']
    return name

def test_str(name):
    assert str(name) == '佐野 七祐'

def test_repr(name):
    assert repr(name) == "Name(gender='female', first=['七祐', 'なゆ', 'ナユ', 'Nayu'], last=['佐野', 'さの', 'サノ', 'Sano'])"

def test_kanji(name):
    assert name.kanji == '佐野 七祐'

def test_hiragana(name):
    assert name.hiragana == 'さの なゆ'

def test_katakana(name):
    assert name.katakana == 'サノ ナユ'

def test_romaji(name):
    assert name.romaji == 'Nayu Sano'
