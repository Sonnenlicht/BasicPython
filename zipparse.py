#! python3

def parse_row(colordat):
    splitdat = list(colordat.split('\n'))
    for i in range(len(splitdat)):
        splitdat[i] = splitdat[i].split(',')
    print(splitdat)
    new_dict = dict(zip(*splitdat))
    print(new_dict)

color_data = "purple,indigo,red,blue,green\n0.15,0.25,0.3,0.05,0.25"
parse_row(color_data)
    
