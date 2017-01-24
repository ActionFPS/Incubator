import json

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

def combine(nicks, keys, admins, clans):
    lines = []
    nicks = json.loads(nicks)
    admins = admins.split("\n")
    clans = json.loads(clans)
    for key in keys.split("\n"):
        try:
            (k, v) = tuple(key.split("="))
            (u, x) = tuple(k.split("."))
        except:
            continue
        if x == "privkey":
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
                    parts.append("privkey=%s" % v)
                    lines.append(" ".join(parts))
    return "\n".join(lines)

if __name__ == "__main__":
    import urllib2
    admins = open('admins.txt').read()
    clans = open('clans.json').read()
    players = open('players.json').read()
    keys = open('keys.properties').read()
    print combine(players, keys, admins, clans)
