import functools
file = open('inputNew.txt')

rules = []
for line in file:
    if line.isspace() : break
    rules.append(list(map(int, line.split('|'))))
    
cache = {}
for x, y in rules:
    cache[(x, y)] = -1
    cache[(y, x)] = 1

def is_ordered(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            k = (update[i], update[j])
            if k in cache and cache[k] == 1:
                return False
    return True
    
def compare(x, y):
    return cache.get((x, y), 0)

t = 0
for line in file:
    update = list(map(int, line.split(',')))
    if is_ordered(update): continue
    update.sort(key=functools.cmp_to_key(compare))
    t += update[len(update) // 2]

print(t)        


