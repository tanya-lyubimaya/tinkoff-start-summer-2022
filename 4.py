n = int(input())
matrix = [["x" for col in range(n)] for row in range(n)]
alphabet = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j", 10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z"}

for i in range(n):
    matrix[i][i] = 0
    matrix[i][n-1-i] = 0
for a in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "x":
                if i >=1 and j >= 1 and matrix[i-1][j] != "x" and matrix[i][j-1] == matrix[i-1][j]:
                    if int(matrix[i][j-1])+1 > 25:
                        matrix[i][j] = 0
                    else:
                        matrix[i][j] = int(matrix[i][j-1])+1
                if i < n-1 and j >= 1 and matrix[i][j-1] != "x" and matrix[i][j-1] == matrix[i+1][j]:
                    if int(matrix[i][j-1])+1 > 25:
                        matrix[i][j] = 0
                    else:
                        matrix[i][j] = int(matrix[i][j-1])+1
                if i >= 1 and j < n-1 and matrix[i-1][j] != "x" and matrix[i-1][j] == matrix[i][j+1]:
                    if int(matrix[i-1][j])+1 > 25:
                        matrix[i][j] = 0
                    else:
                        matrix[i][j] = int(matrix[i-1][j])+1
                if i < n-1 and j < n-1 and matrix[i][j+1] != "x" and matrix[i][j+1] == matrix[i+1][j]:
                    if int(matrix[i+1][j])+1 > 25:
                        matrix[i][j] = 0
                    else:
                        matrix[i][j] = int(matrix[i+1][j])+1

for i in range(n):
    for j in range(n):
        print(alphabet[matrix[i][j]], end="")
    print("")