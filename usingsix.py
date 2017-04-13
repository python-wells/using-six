#!/usr/bin/env python
# coding=utf-8

"""common usage of the six library.

https://pythonhosted.org/six/

"""

import six


def test_string():
    assert type(u"abc") is six.text_type
    assert type(b"abc") is six.binary_type
    assert type(six.u("abc")) is six.text_type
    assert type(six.b("abc")) is six.binary_type


def test_stringio():
    f = six.BytesIO()
    f.write(b"abc\n")
    assert f.getvalue() == b"abc\n"

    f = six.StringIO()
    f.write(u"abc\n")
    assert f.getvalue() == u"abc\n"


def test_iteritem():
    d = {
        "a": 1,
        "b": 2,
    }
    for k, v in six.iteritems(d):
        print(k, v)


def test_range():
    assert 2 in six.moves.range(3)


def test_pickle():
    d = [1, 2, 3]
    byte_str = six.moves.cPickle.dumps(d)
    obj = six.moves.cPickle.loads(byte_str)
    assert obj == d


def using_input():
    r = six.moves.input("Install directory: ")
    return r


def test_urlparse():
    url = "http://www.example.com/foo?q=abc"
    r = six.moves.urllib.parse.urlparse(url)
    assert r.scheme == 'http'
    assert r.path == '/foo'
