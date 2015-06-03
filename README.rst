Gimei
=====

|Downloads| |Supported Python versions| |Latest Version| |License|

This package generates the name and the address at random.

Original is `gimei <https://github.com/willnet/gimei>`__. Thank's
@willnet

Installation
------------

.. code:: sh

    $ pip install gimei

Usage
-----

.. code:: python

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

Recommendation
--------------

``pyyaml`` is very convenient, but it's for a short while later to deal
with a great deal of data. It's recommended hard to install
`libyaml <http://pyyaml.org/wiki/LibYAML>`__.

License
-------

MIT

Author
------

Mao Nabeta

`twitter <https://twitter.com/nabetama>`__

.. |Downloads| image:: https://pypip.in/download/gimei/badge.svg
   :target: https://pypi.python.org/pypi/gimei/
.. |Supported Python versions| image:: https://pypip.in/py_versions/gimei/badge.svg
   :target: https://pypi.python.org/pypi/gimei/
.. |Latest Version| image:: https://pypip.in/version/gimei/badge.svg?text=version
   :target: https://pypi.python.org/pypi/gimei/
.. |License| image:: https://pypip.in/license/gimei/badge.svg
   :target: https://pypi.python.org/pypi/gimei/
