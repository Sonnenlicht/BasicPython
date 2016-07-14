#! python3

routes = {101: ("Tumwater, Washington", "Los Angeles, California"),
66: ("Chicago, Illinois", "Santa Monica, California")}

def printroutes(route):
    for k, v in route.items():
        print('Route ' + str(k) + ' goes from ' + str(v[0]) + ' to ' + str(v[1]))

printroutes(routes)
