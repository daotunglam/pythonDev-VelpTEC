def stringtodict(s):
    s = s.strip()
    s = s.lstrip('{')
    s = s.rstrip('}')
    d = {}
    for pair in s.split(','):
        k, v = pair.split(':')
        k = str(k)
        v = int(v)
        d[k] = v
    return d

print(stringtodict('{"1. Key": 34, "2. Key": 446, "3. Key": 4}'))