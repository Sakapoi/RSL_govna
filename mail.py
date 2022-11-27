matrix = [
    [0,1,0,0],
    [0,0,0,1],
    [0,1,0,0],
    [0,0,1,0]
]

def proverka2(matrix, a, b, visited=[]):
    
    if(matrix[a][b]==1): return True#1- 
    else: 
        for i in range(0,len(matrix[a])):
            if matrix[a][i]==1 and not visited[i]:
                visited[i]=True
                if proverka2(matrix, i, b, visited): return True

    return False

def proverka(matrix, a, b):
   return proverka2(matrix, a, b, [0 for _ in range (0,len(matrix[0]))])


print(proverka(matrix, 3, 2)==True)
print(proverka(matrix, 1, 0)==False)
print(proverka(matrix, 1, 2)==True)


print("hyillo")

