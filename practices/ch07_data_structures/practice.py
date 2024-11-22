d = {
    'Sam': 7,
    'Sarah': 'None',
    'Jeff': -1,
    'rolls': ['rock', 'paper', 'scissors'],
    'done': 'true'
}

print(d["Sam"])          # outputs 7
print(d['rolls'])        # outputs ['rock', 'paper', 'scissors']
print(d.get('Sarah'))    # outputs None
print(d.get('Jeff', -1)) # outputs -1
print(d['done'])         # outputs True
