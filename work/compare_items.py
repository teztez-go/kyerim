import json, re

with open("kyerim-equipment.html") as f:
    text = f.read()

m = re.search(r'const PRESET_GYERIM = (\[.*?\]);', text, re.DOTALL)
current_items = json.loads(m.group(1))

with open("work/inspect_user_json.py") as f:
    # Read user_json
    import subprocess

from inspect_user_json import items as user_items

print(f"Current items count: {len(current_items)}")
print(f"User items count: {len(user_items)}")

# Check if IDs match or what changed
curr_map = {it['id']: it for it in current_items}
user_map = {it['id']: it for it in user_items}

added_ids = set(user_map.keys()) - set(curr_map.keys())
removed_ids = set(curr_map.keys()) - set(user_map.keys())

print(f"Added IDs in user_json: {added_ids}")
print(f"Removed IDs from current: {removed_ids}")

# Check any price/qty/name/note changes on matching IDs
changed = []
for k in set(user_map.keys()) & set(curr_map.keys()):
    c = curr_map[k]
    u = user_map[k]
    diffs = {}
    for field in ['name', 'price', 'qty', 'zone', 'note']:
        if c.get(field) != u.get(field):
            diffs[field] = (c.get(field), u.get(field))
    if diffs:
        changed.append((c['name'], diffs))

print(f"Changed items count: {len(changed)}")
for name, diffs in changed:
    print(f"  {name}: {diffs}")
