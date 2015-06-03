# Gimei

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

print name
print name.kanji
print name.hiragana
print name.katakana
print name.last.kanji
print name.last.hiragana
print name.last.katakana
print name.first.kanji
print name.first.hiragana
print name.first.katakana


address = Gimei().address

print address
print address.kanji
print address.hiragana
print address.katakana

print address.prefecture.kanji
print address.prefecture.hiragana
print address.prefecture.katakana

print address.city.kanji
print address.city.hiragana
print address.city.katakana

print address.town.kanji
print address.town.hiragana
print address.town.katakana
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
