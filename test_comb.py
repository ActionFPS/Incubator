import pytest
from comb import *

def test_tag_match():
    assert match_tag('w00p|*', 'w00p|Drakas')
    assert not match_tag('w00px|*', 'w00p|Drakas')
    assert not match_tag('*|w00p', 'Drakas|w00pp')
    assert match_tag('*|w00p', 'Drakas|w00p')
    assert match_tag('*|DnC|*', '|DnC|madcatz')

keys=("#abc\n\ndrakas.private-key=ABCD\ndrakas.public-key=ABDY")
admins = ["drakas", "lucas", "sanzo"]

def test_comb():
    nicknames=json.loads('[{"id": "drakas", "nickname": {"nickname": "w00p|Drakas"}}]')
    clans = json.loads('[{"id": "woop", "tag": "w00p|*"}]')
    # https://actionfps.com/clans/?format=json
    expected_output = "id=drakas nickname=w00p|Drakas admin group=woop pubkey=ABDY"
    assert(list(combine(nicknames, keys, admins, clans)) == [expected_output])
