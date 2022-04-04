def make_grid(filename):

    with open(filename, "r") as file:
        rows = file.readlines()
        print(rows)
        tab = []
        for i in range(len(rows)):
            for j in range
