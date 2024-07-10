import re

def extractor(chall):
    pattern = r'/%(?!20)[0-9a-fA-F]{2}(?=\b)'
    hid_val = []
    with open(chall, 'r') as f:
        for line in f:
            matches = re.findall(pattern, line)
            hid_val.extend(matches)
    return hid_val

def save(chall, data):
    with open(chall, 'w') as f:
        for item in data:
            f.write(f"{item}\n")

chall = '../release/chall/access.log'
hid_val = extractor(chall)

result = 'result.txt'
save(result, hid_val)
