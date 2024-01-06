import random

def generate(n: int) -> list:
        field = [[],[],[],[]]
        for i in range(0, 4):
            for j in range(0, 4):
                if random.randint(0,100) < 26:
                    field[i].append(-1)
                else:
                    field[i].append(0)

        for i in range(0, 4):
            for j in range(0, 4):
                if field[i][j] != -1:
                    if j != 3:
                        if field[i][j+1] == -1:
                            field[i][j] += + 1
                    if j != 0:
                            if field[i][j-1] == -1:
                                field[i][j] += + 1
                    if i != 0:
                        if field[i-1][j] == -1:
                            field[i][j] += + 1
                        if j != 0:
                            if field[i-1][j-1] == -1:
                                field[i][j] += + 1
                        if j != 3:
                            if field[i-1][j+1] == -1:
                                field[i][j] += + 1
                    if i != 3:
                        if field[i+1][j] == -1:
                            field[i][j] += + 1
                        if j != 0:
                            if field[i+1][j-1] == -1:
                                field[i][j] += + 1
                        if j != 3:
                            if field[i+1][j+1] == -1:
                                field[i][j] += + 1
        return field
