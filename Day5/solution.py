with open('inputNew.txt') as file:
    content = file.read()
    
sections = content.strip().split('\n\n')



first_section = [line.split("|") for line in sections[0].split('\n')]
rules = [(int(a), int(b)) for a, b in first_section]

updates = [list(map(int, line.split(","))) for line in sections[1].split("\n")]

correct = []
t = 0
for update in updates:
    checker = True
    for i in range(len(update)):
        for j in range(len(update)):
            if i != j:
                if (update[min(i, j)], update[max(i, j)]) not in rules:
                    checker = False
    if checker:
        t += update[len(update) // 2]
    
print(t)


#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⢲⣦⡀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⠖⠚⠓⠒⠒⠲⠿⣍⣛⣻⣦⣷⢠⣻⣀⠤⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⡿⠓⠲⠬⢥⡤⠤⠤⠤⠤⣤⣀⣀⣈⣻⣿⣿⠓⠉⣀⡤⠔⢶⣻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⢤⠞⠁⣼⠀⠀⠀⠀⠀⠀⠰⠶⢌⣽⡶⠟⢏⡁⢈⣉⣭⣷⡯⣝⠒⢦⣄⠙⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⣵⠿⣳⡟⠉⠉⠿⠀⠀⡀⠀⠀⣀⣀⣢⣾⣿⡚⠓⠒⠒⠒⠻⢿⣟⣧⡀⢠⣢⡻⠙⣄⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⢿⣟⣲⢿⣷⢀⣤⣠⣄⣈⢿⣷⣤⣷⣻⡓⠒⠻⠭⢷⡄⠒⠲⢶⣦⣬⣻⣏⢦⡈⢿⣆⠘⡄⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢖⣩⠷⢎⣙⣿⣿⣼⡼⣿⣟⣽⣻⢯⢿⠞⣌⠙⢳⡕⠀⠙⠲⣶⠤⢄⡠⣄⡈⠛⣿⣿⣧⢳⣌⢻⡆⡇⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠗⠉⢀⣾⠟⠒⡿⣫⡿⡾⢫⢟⡏⠉⢸⡀⠑⢾⡆⢤⣻⣶⣤⣘⣲⣿⣶⡽⠿⣯⠲⣌⣇⢹⣷⣿⣆⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⡼⠀⣿⢣⣧⠋⣸⠀⣰⢀⣿⣆⠀⠰⣄⠙⣧⣨⣿⣿⣿⣯⣿⣦⠘⣷⡌⢻⡄⠿⣆⠟⣆⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡼⣹⠈⢣⠆⡇⣰⣻⣼⣿⣽⣷⣦⣹⣿⣟⣯⠉⠘⣿⠏⠃⠀⣷⣽⡿⣾⡹⣷⣹⣧⡈⢺⡀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⣷⣱⣽⡀⢸⣆⢳⣿⣇⣷⡿⠖⠿⠷⢦⣙⣆⠩⡗⠀⠀⠀⠀⠀⡯⠿⠳⣟⠻⣽⣄⢧⠈⠳⣷⡀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣷⣸⣿⡀⣿⣅⠛⠇⠀⠀⠀⠀⢈⠙⠂⠀⠀⠀⠀⠀⣸⣿⠀⢠⣜⢦⠘⢿⣮⣷⡀⠀⠙⢦⡀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⢯⣇⠙⢄⣀⠀⠀⠀⢀⣀⡠⣴⣾⣫⠵⠛⣿⣻⠿⣷⣹⣾⣷⡠⡀⠀⠀⠀⠻⠦⠀⣀⠔⠀⠀⣴⣿⣸⣧⡀⠳⣝⠳⢴⡙⢞⣏⠢⡀⠀⠹⡄⠀
#⠀⠀⠀⠀⠀⠀⢀⣀⣀⣈⣻⣤⣀⠈⠉⠻⠿⢿⣺⣿⡵⣶⢶⣦⠀⠘⣿⢷⣾⢿⣿⡋⢙⣮⣄⡀⠀⠀⠉⠈⠀⠀⢀⢞⣿⣼⣿⣿⣿⣆⡀⠙⢦⣝⣮⠛⢷⡙⢆⠀⣷⠀⠀
#⠀⠀⠀⢠⡴⢟⣫⠤⠖⠒⠛⢛⣲⣿⣿⣿⠟⠋⢱⣿⣴⣷⣿⣹⢃⣀⣘⠃⢩⢿⣫⣥⣿⠧⢿⣿⣗⡶⣤⣄⣀⣴⣷⣻⣿⣿⠻⠘⣏⠛⢿⣦⣀⠱⢤⣉⡑⠛⠮⢿⣹⠀⠀⠀
#⠀⢠⢖⠵⠊⠁⢀⡤⠖⣲⣿⣿⣟⣻⣿⣋⠀⠀⠈⢿⣿⡿⠟⣵⣿⣿⣿⣷⡏⠈⢿⡿⣷⣤⣼⢿⣿⣿⢶⣯⣭⣵⣾⢿⣿⠿⢦⡀⢹⠀⠈⣏⠉⠉⢻⣶⣯⡑⠦⣄⠈⠳⣄⠀
#⠀⠹⠁⠀⠀⣞⢁⡾⢽⣯⣝⣛⣛⣯⣭⣽⣿⣷⣶⣤⣤⣴⣿⣿⣿⣿⣿⣿⡀⣀⣼⣀⠈⠙⠛⠷⣾⡿⢿⡟⣿⠟⠁⣈⣥⡴⠾⠷⢾⡄⠀⣿⠀⠀⠈⢇⠘⣿⣤⣀⠑⢦⡘⢧⠀
#⠄⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⡿⠛⣻⢏⡽⣯⡄⠘⣏⣿⡏⠈⠙⠓⠶⣤⣀⠀⠙⢿⣿⡇⢀⡿⠋⠁⠀⢀⣀⣸⡇⠀⣟⣀⠀⠀⠀⠙⠃⣿⡎⠑⣤⡙⣌⡇
#⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⡥⣖⡯⠖⢋⣡⡞⣼⣿⠀⠀⢹⣿⣷⠀⠀⣀⡀⠀⠉⠻⣦⠀⢿⣿⡿⠁⣠⡶⠟⠋⠉⠹⣆⣸⣿⣿⠀⣀⡤⣤⡀⣿⠇⠀⢸⠳⡜⡇
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣿⣿⣿⣿⣿⣿⣏⢿⣗⠒⠊⠉⢸⠁⡿⡏⠀⢀⣿⡿⣁⠤⢶⣿⣽⡆⠀⠀⠘⢷⡈⠉⣡⠾⠋⠀⠀⣠⣆⢠⣿⣿⣿⡟⢀⣷⠒⢺⣧⡏⠀⠀⢸⠀⢹⣹
#⠀⠀⠀⠀⠀⠀⠀⡠⢪⠟⡽⠙⢶⣾⣿⣿⣿⣷⡻⣦⡀⠀⠀⢣⣇⡇⢀⡞⣸⠏⠁⠀⠀⡇⢻⡀⠀⠀⣾⣶⡟⣿⣥⡄⠀⠀⢠⣇⣼⡶⣿⣿⠋⣸⣾⣷⣚⣽⡟⠀⠀⠀⣏⠀⡼⣿
#⠀⠀⠀⠀⠀⢀⠎⡴⣣⣾⠟⣡⠞⢹⡿⣿⢿⣿⣿⣿⣷⣄⠀⠈⠻⡹⣼⠀⣿⡄⠀⠀⠀⠉⠻⣷⡀⠀⠙⠿⠇⣿⠿⠇⠀⠀⢠⡿⠋⢇⢹⣟⢷⠫⣿⣟⡿⠋⠀⠀⣠⣾⢞⡜⠁⡿
#⠀⠀⠀⠀⠀⡼⡼⣵⠏⡏⣰⠃⠀⢾⡇⠈⠻⣿⣮⡉⠹⣿⣧⣄⡀⠙⣇⠀⠸⣿⣄⡀⠀⠀⠀⠈⢉⣧⡴⠀⠠⡄⣀⡤⠤⠴⠋⠁⠀⠈⢻⣿⣾⣤⡿⠋⠀⠀⠀⣉⣽⠿⠋⠀⣰⠃
#⠀⠀⠀⠀⠀⣿⣽⠋⠀⡇⡇⠀⠀⠘⣷⢠⣶⢮⣻⣿⣦⠈⠛⠙⠹⣷⠘⢦⣤⣿⣳⣭⣑⣒⣒⣺⣿⢿⣀⣀⣀⣿⣧⣀⣀⣀⡤⠴⠒⣶⣿⣏⣾⡿⠁⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⢻⡏⠀⠀⢳⣇⠀⠀⠀⠈⠈⣿⣾⣿⣿⣮⣿⣦⠀⠀⢿⣶⡫⣿⣿⣿⣿⣿⡹⣯⣊⠁⠉⠉⠉⠉⢙⣮⣷⣶⡤⣤⣶⣿⣿⣟⣾⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠸⣿⣦⡀⠀⠙⠦⠀⠀⢀⣼⠿⣽⣿⣯⣷⣼⡷⢾⣻⣾⣿⠞⢿⢻⡷⠻⣿⣏⡙⢝⣻⡾⡖⠒⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣎⠣⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⣴⣋⣉⣩⣿⣿⢿⣟⣷⣾⣯⡟⢱⡇⠀⠘⣿⠣⡀⣈⣻⣿⣿⣿⣷⣷⣶⣿⣿⣟⠋⡿⣹⣿⣿⣿⣿⢟⣏⠺⠿⠶⠭⠷⠂⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⢹⣮⣾⣿⡿⢋⣶⢸⡇⠀⠀⠈⢷⡑⠈⢻⣟⠛⠛⠿⠋⠙⠓⣭⣿⣹⣵⣿⣿⣿⣿⣿⠈⠻⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢟⣛⡭⠶⢾⡿⠃⠀⠀⢸⢹⣾⣇⠀⠀⠀⠀⠻⣟⣿⡏⠀⠀⠀⠀⢰⣿⣿⢿⡇⣿⣿⣿⣿⣟⡏⠀⠀⠀⠉⠙⠓⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⢰⣿⢸⣿⢿⡀⠀⠀⠀⠀⢸⣿⣣⠀⠀⠀⢠⣿⡟⣷⣾⣿⢿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠁⠀⠀⠀⠘⡿⡿⢿⣏⣧⠀⠀⠀⢀⣾⣿⠿⠀⢀⣴⣿⣿⢿⡹⡇⣿⠈⣿⣿⡟⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⢳⢧⠈⢿⣿⠀⠀⢀⣼⣿⠕⠁⣠⣾⡿⣻⠏⠀⢹⣹⣿⣆⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣷⠀⠀⠀⠀⠈⣏⢧⠀⢻⣧⠶⣋⠿⠋⣀⣾⣟⣿⠞⠁⠀⠀⠀⢯⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣇⠀⠀⠀⠀⠸⡜⣆⠈⢷⣿⠀⢠⣾⣿⠟⢻⡏⠀⠀⠀⠀⠀⠘⣿⣿⠏⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡻⣿⣿⣦⡀⠀⠀⠀⢧⠘⣆⠈⢷⠒⠛⢻⡿⠄⠘⣧⠀⠀⠀⠀⠀⢰⣷⣹⠀⠙⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⣝⣿⣿⣷⣄⠀⠀⠈⢇⠸⡄⠈⣇⠀⠀⢻⣆⠀⠘⣇⠀⠀⣠⣾⣽⢹⡟⠀⢰⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣾⢻⠙⢿⣿⡇⠀⠀⠈⢧⢳⠀⢸⡀⠀⠀⢻⣆⠀⢻⡄⢠⣿⣯⣽⣓⣧⣤⠾⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣼⡇⠀⠙⣿⠀⠀⠀⠈⢏⢧⠀⣇⠀⠀⠀⢻⣆⠀⢷⠘⣿⣮⡻⣿⠁⠀⢀⣯⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠘⡾⡄⢸⠀⠀⠀⠈⢻⣆⠈⢷⣷⣾⣟⣻⣶⣿⡿⠛⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⢳⣇⠘⡆⠀⠀⠀⠀⠻⣶⢺⡏⢹⡟⠀⠉⠁⠀⠀⠀⢩⣍⠙⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣟⣿⣿⣿⣧⠀⢀⣤⣤⡸⣸⠀⡇⠀⠀⠀⠀⠀⠙⣿⣷⢡⣿⣶⣄⠀⠀⣄⠀⣦⣍⠙⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡿⢿⡙⠿⠀⢸⡟⢲⣷⡿⡄⢿⠀⠀⠀⠀⠀⠀⠘⣏⢸⣇⣍⢻⣷⣀⢻⣦⣤⣌⡙⣦⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣯⢷⠀⠀⠸⡇⠀⢿⣧⡇⢸⠀⠀⠀⠀⠀⠀⠀⣼⢸⣿⣯⠀⣿⣿⣷⣝⣿⣻⣿⣼⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣎⣧⠀⠐⣇⠀⠘⣽⣿⡸⡆⠀⠀⠀⠀⠀⠀⠈⠋⠈⠻⣼⣿⢶⢿⣿⣯⡻⣿⣿⣾⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡼⡆⠀⣿⡀⠀⣿⢿⡇⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣾⢧⠈⠙⠿⣮⠟⠉⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⢻⢠⣿⡇⠀⠹⣄⢳⣜⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡏⠪⠳⢤⣄⣀⠀⠀⠀⠈⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣎⣿⡟⡇⠀⠀⠈⢻⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡄⠀⠀⠀⠙⢧⡀⢀⡄⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀