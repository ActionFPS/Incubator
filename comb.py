import json

def match_tag(tag, nickname):
    if tag.startswith("*") and tag.endswith("*"):
        return tag[1:-1] in nickname
    elif tag.startswith("*"):
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

def combine(nicks, keys, admins, clans):
    lines = []
    admins = admins
    for key in keys.split("\n"):
        try:
            (k, v) = tuple(key.split("="))
            (u, x) = tuple(k.split("."))
        except:
            continue
        if x == "public-key":
            for n in nicks:
                if n['id'] == u:
                    nick = n['nickname']['nickname']
                    parts = []
                    parts.append("id=%s" % u)
                    parts.append("nickname=%s" % nick)
                    if u in admins:
                        parts.append("admin")
                    for clan in clans:
                        if clan_matches(clan, nick):
                            parts.append("group=%s" % clan['id'])
                    parts.append("pubkey=%s" % v)
                    yield " ".join(parts)

def combine_files(n,k,a,c):
    admins = open(a).read()
    clans = open(c).read()
    players = open(p).read()
    keys = open(k).read()
    print combine(players, keys, admins, clans)

if __name__ == "__main__":
    with open('players.json') as f:
        players = json.loads(f.read())
    with open('admins.txt') as f:
        admins = f.read().splitlines()
    with open('keys.properties') as f:
        keys = f.read()
    with open('clans.json') as f:
        clans = json.loads(f.read())
    for line in combine(players, keys, admins, clans):
        print line
