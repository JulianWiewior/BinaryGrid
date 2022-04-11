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
            if matrix[row][k]==str(j):
                if matrix[row][k]==matrix[row][k+1]==matrix[row][k+2]:
                    return False
    return True

def Unikalne(matrix, row, kol):
    '''
    :param matrix: macierz
    :return: True, jezeli kazdy wiersz i kolumna sa unikalne, w przeciwnym razie False
    '''
    czyPuste = False
    if 'x' in matrix[row]:
        czyPuste = True
    for i in range(len(matrix)):
        if i!=row:
            if np.array_equal(matrix[i], matrix[row]):
                return False
    nowymatrix = matrix.T
    for i in range(len(nowymatrix)):
        if i!=kol:
            if np.array_equal(nowymatrix[i], nowymatrix[kol]):
                return False
    return True, czyPuste

    #
    #
    # for i in range(0, len(matrix)-1):
    #     for j in range(i+1, len(matrix)):
    #         licznik = 0
    #         for k in range(len(matrix)):
    #             if matrix[k][i]==matrix[k][j]:
    #                 licznik+=1
    #         if licznik==len(matrix):
    #             return False
    # # Do powyższych pętli:
    # #     i - główna kolumna, od której sprawdzamy
    # #     j - kolumna któraś z prawej, którą sprawdzamy
    # #     k - wiersz, dla którego porównujemy (idziemy w dół)
    #
    # for i in range(0, len(matrix)-1):
    #     for j in range(i+1, len(matrix)):
    #         licznik = 0
    #         for k in range(len(matrix)):
    #             if matrix[i][k]==matrix[j][k]:
    #                 licznik+=1
    #         if licznik==len(matrix):
    #             return False
    #
    # # Do powyższych pętli:
    # #     i - główny wiersz, od którego sprawdzamy
    # #     j - wiersz któryś z dołu, który sprawdzamy
    # #     k - kolumna, dla której porównujemy (idziemy w prawo)
    # return True

def TyleSamo(matrix, row, kol, field):
    '''
    :param matrix: macierz
    :return: True, jeżeli każdy wiersz i kolumna zawierają tyle samo 0 co 1, w przeciwnym razie False
    '''
    for j in field:
        liczba = 0
        for i in range(len(matrix)):
            if matrix[row][i]==str(j):
                liczba+=1
        if(liczba>len(matrix)/2):
            return False
        liczba = 0
        for i in range(len(matrix)):
            if matrix[i][kol]==str(j):
                liczba+=1
        if(liczba>len(matrix)/2):
            return False
    return True

def puste(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]=='x':
                return i,j
    return False

def sprawdzenie(matrix, i, j, field):
    if Trojki(matrix,i,j,[0,1]) == False or Unikalne(matrix, i, j) == False or TyleSamo(matrix, i, j, field)==False:
        return False
    return True

def solve(matrix, field):
    punkt = puste(matrix)
    if punkt == False:
        print(matrix)
        return

    row = punkt[0]
    kol = punkt[1]


    for i in field:
        matrix[row][kol]=str(i)
        if sprawdzenie(matrix,row,kol,field)==True:
            solve(matrix, field)

    matrix[row][kol]='x'
    return

solve(make_grid("binary_10x10"),[0,1])