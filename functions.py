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

def Unikalne(matrix):
    '''
    :param matrix: macierz
    :return: True, jezeli kazdy wiersz i kolumna sa unikalne, w przeciwnym razie False
    '''

    for i in range(0, len(matrix)-1):
        for j in range(i+1, len(matrix)):
            licznik = 0
            for k in range(len(matrix)):
                if matrix[k][i]==matrix[k][j]:
                    licznik+=1
            if licznik==len(matrix):
                print("kolumna")
                return False
    # Do powyższych pętli:
    #     i - główna kolumna, od której sprawdzamy
    #     j - kolumna któraś z prawej, którą sprawdzamy
    #     k - wiersz, dla którego porównujemy (idziemy w dół)

    for i in range(0, len(matrix)-1):
        for j in range(i+1, len(matrix)):
            licznik = 0
            for k in range(len(matrix)):
                if matrix[i][k]==matrix[j][k]:
                    licznik+=1
            if licznik==len(matrix):
                print("wiersz")
                return False

    # Do powyższych pętli:
    #     i - główny wiersz, od którego sprawdzamy
    #     j - wiersz któryś z dołu, który sprawdzamy
    #     k - kolumna, dla której porównujemy (idziemy w prawo)
    return True

def TyleSamo(matrix):
    '''
    :param matrix: macierz
    :return: True, jeżeli każdy wiersz i kolumna zawierają tyle samo 0 co 1, w przeciwnym razie False
    '''
    for i in range(len(matrix)):
        ilezer = 0
        ilejedynek = 0
        for j in range(len(matrix)):
            if matrix[i][j]=="0":
                ilezer+=1
            if matrix[i][j]=="1":
                ilejedynek+=1
        if ilezer!=ilejedynek:
            return False
    for i in range(len(matrix)):
        ilezer = 0
        ilejedynek = 0
        for j in range(len(matrix)):
            if matrix[j][i]=="0":
                ilezer+=1
            if matrix[j][i]=="1":
                ilejedynek+=1
        if ilezer!=ilejedynek:
            return False

    return True
print(TyleSamo(make_grid("binary_test1.txt")))