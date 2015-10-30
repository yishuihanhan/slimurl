#!/usr/bin/env python
# encoding: utf-8
from slimurl import URL


def check_gt(url_a, url_b, expected_result):
    assert (URL(url_a) > URL(url_b)) == expected_result, \
        "Unexpected result: %r > %r is not %s" % (url_a, url_b, expected_result)


def test_gt():
    cases = {
        ("http://example.net:80", "http://example.net/", False),
        ("http://example.net:80", "http://example.net", False),
        ("http://example.net:8080", "http://example.net", True),
        ("http://example.net/?bar=foo&foo=bar", "http://example.net/?foo=bar&bar=foo", False),
    }

    for url_a, url_b, expected_result in cases:
        yield check_gt, url_a, url_b, expected_result