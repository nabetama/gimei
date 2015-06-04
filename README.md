# Gimei
[![wercker status](https://app.wercker.com/status/2e16506f61d42fa320a681aac332b30d/m "wercker status")](https://app.wercker.com/project/bykey/2e16506f61d42fa320a681aac332b30d)

This package generates the name and the address at random.

Original is [gimei](https://github.com/willnet/gimei).
Thank's @willnet

## Installation
```sh
$ pip install gimei
```

## Usage

```python
from gimei import Gimei

name = Gimei().name

print name                # 川端 一世 
print name.kanji          # 川端 一世
print name.hiragana       # かわばた ひとせ
print name.katakana       # カワバタ ヒトセ
print name.last.kanji     # 川端
print name.last.hiragana  # かわばた
print name.last.katakana  # カワバタ
print name.first.kanji    # 一世
print name.first.hiragana # ひとせ
print name.first.katakana # ヒトセ


address = Gimei().address 

print address             # 大分県三潴郡大木町小原西
print address.kanji       # 大分県三潴郡大木町小原西
print address.hiragana    # おおいたけんみずまぐんおおきまちこばらにし
print address.katakana    # オオイタケンミズマグンオオキマチコバラニシ

print address.prefecture.kanji     # 大分県
print address.prefecture.hiragana  # おおいたけん
print address.prefecture.katakana  # オオイタケン

print address.city.kanji     # 三潴郡大木町
print address.city.hiragana  # みずまぐんおおきまち
print address.city.katakana  # ミズマグンオオキマチ

print address.town.kanji     # 小原西
print address.town.hiragana  # こばらにし
print address.town.katakana  # コバラニシ
```

## Recommendation

`pyyaml` is very convenient, 
but it's for a short while later to deal with a great deal of data.
It's recommended hard to install [libyaml](http://pyyaml.org/wiki/LibYAML).

## License
MIT

## Author
Mao Nabeta

[twitter](https://twitter.com/nabetama)
