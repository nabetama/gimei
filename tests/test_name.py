# coding: utf-8
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

    def test_str(self):
        name = Gimei().name
        name.first.all = ['糸央', 'いお', 'イオ']
        name.last.all  = ['大木', 'おおき', 'オオキ']
        assert str(name) == '大木 糸央'

    def test_create_name_from_gender(self):
        name = Gimei('male').name
        assert name.is_male

    def test_create_name_from_gender(self):
        name = Gimei('female').name
        assert name.is_female
