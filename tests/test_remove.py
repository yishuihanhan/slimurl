#!/usr/bin/env python
# encoding: utf-8
from slimurl import URL


def check_remove(url_a, key, url_b):
    url_a.remove(key)
    assert url_a == url_b


def test_remove_all():
    cases = [
        ["http://example.net/?foo=bar", "foo", "http://example.net/"],
        ["http://example.net/?foo=", "foo", "http://example.net/"],
        ["http://example.net/?foo", "foo", "http://example.net/"],
        ["http://example.net/?foo=foo&foo=bar", "foo", "http://example.net/?foo=foo"],
    ]

    for url_a, key, url_b in cases:
        yield check_remove, URL(url_a), key, URL(url_b)
