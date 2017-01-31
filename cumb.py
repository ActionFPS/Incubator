import json
import urllib
import os
import base64
players = json.loads(urllib.urlopen('https://actionfps.com/players/?format=json').read())
clans = json.loads(urllib.urlopen('https://actionfps.com/clans/?format=json').read())
users = []
groups = []

def match_tag(tag, nickname):
    if tag.startswith("*"):
        return nickname.endswith(tag[1:])
    elif tag.endswith("*"):
        return nickname.startswith(tag[:-1])

def clan_matches(clan, nickname):
    if 'tag' in clan:
        return match_tag(clan['tag'], nickname)
    elif 'tags' in clan:
        for tag in clan['tags']:
            if match_tag(tag, nickname):
                return True
    return False

def gen_user(id):
    user = ['id=%s' % id]
    with open(item) as f:
        user.append("pubkey=%s" % base64.b64encode(f.read()))
    for player in players:
        if player['id'] == id:
            nickname = player['nickname']['nickname']
            user.append('name=%s' % nickname)
            for clan in clans:
                if clan_matches(clan, nickname):
                    user.append('group=%s' % clan['id'])
    if len(user) < 2:
        return None
    else:
        return user

for item in os.listdir('.'):
    if item.endswith('.pub'):
        user = gen_user(id = item.split(".")[0])
        if user:
            users.append(" ".join(user))

for clan in clans:
    group = ["id=%s" % clan['id'], 'name=%s' % clan['name']]
    groups.append(" ".join(group))

with open('users.db', 'w') as f:
    f.write("\n".join(users))

with open('groups.db', 'w') as f:
    f.write("\n".join(groups))
