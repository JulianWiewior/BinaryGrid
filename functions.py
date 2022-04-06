import numpy as np
def make_grid(filename):
    '''
    funkcja przetwarza dany plik w macierz
    :param filename: plik z macierza
    :return: przygotowana w liscie macierz
    '''

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

def Trojki(matrix, row, kol, field):
    '''
    funkcja sprawdza, czy w wierszu i kolumnie sa jakies trojki
    :param matrix: macierz
    :param row: indeks wiersza
    :param kol: indeks kolumny
    :param field: dziedzina przeszukiwania
    :return:
    '''
    for j in field:
        for i in range(len(matrix)-2):
           if matrix[i][kol]==str(j):
                if matrix[i][kol] == matrix[i+1][kol] == matrix[i+2][kol]:
                    return False

        for k in range(len(matrix)-2):
            print(matrix[row][k])
            if matrix[row][k]==str(j):
                if matrix[row][k]==matrix[row][k+1]==matrix[row][k+2]:
                    return False
    return True

