def goto(modes, name):
    return list(filter(lambda x: x.name ==name, modes))[0]