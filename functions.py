import numpy as np
def make_grid(filename):

    with open(filename, "r") as file:
        rows = file.readlines()
        tab = []
        for i in range(len(rows)):
            rows[i]=rows[i].strip()
            pom = []
            for j in range(len(rows)):
                pom.append(rows[i][j])
            tab.append(pom)
        matrix = np.array(tab)
        return matrix
make_grid("binary_6x6")

def Trojki(matrix, row, kol, field):

    for j in field:
        for i in range(len(matrix)-2):
            if matrix[i][kol]==j:
                if matrix[i][kol] == matrix[i+1][kol] == matrix[i+2][kol]:
                    return False

        for k in range(len(matrix)-2):
            if matrix[row][k]==j:
                if matrix[row][k]==matrix[row][k+1]==matrix[row][k+2]:
                    return False
    return True

