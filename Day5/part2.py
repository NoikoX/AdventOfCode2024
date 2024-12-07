with open('test.txt') as file:
    content = file.read()
    
sections = content.strip().split('\n\n')



first_section = [line.split("|") for line in sections[0].split('\n')]
rules = [(int(a), int(b)) for a, b in first_section]

updates = [list(map(int, line.split(","))) for line in sections[1].split("\n")]

incorrect = []
for update in updates:
    checker = True
    for i in range(len(update)):
        for j in range(len(update)):
            if i != j:
                if (update[min(i, j)], update[max(i, j)]) not in rules:
                    checker = False
    if not checker:
        incorrect.append(update)
    
t = 0
for inc in incorrect:
    good = sorted(inc, reverse=True)
    t += good[len(good) // 2]
print(t)
    
