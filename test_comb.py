import pytest
from comb import *

def test_tag_match():
    assert match_tag('w00p|*', 'w00p|Drakas')
    assert not match_tag('w00px|*', 'w00p|Drakas')
    assert not match_tag('*|w00p', 'Drakas|w00pp')
    assert match_tag('*|w00p', 'Drakas|w00p')

def test_comb():
    nicknames='[{"id": "drakas", "nickname": {"nickname": "w00p|Drakas"}}]'
    keys=("#abc\n\ndrakas.privkey=ABCD\ndrakas.pubkey=ABDY")
    admins = ("drakas\nlucas\nsanzo")
    clans = '[{"id": "woop", "tag": "w00p|*"}]'
    # https://actionfps.com/clans/?format=json
    expected_output = "id=drakas nickname=w00p|Drakas admin group=woop privkey=ABCD"
    assert(combine(nicknames, keys, admins, clans) == expected_output)
