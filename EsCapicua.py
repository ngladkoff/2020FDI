#Vectores-EsCapicua

def es_capicua(v, tamanio):    
    
    i1= 0
    i2= tamanio - 1    
    
    while i1 < i2:
        if v[i1] != v[i2]:
            return False
        else:
            i1 = i1 + 1
            i2 = i2 - 1    

    return True


vector1 = [40,3,25,6,25,3,40]
vector2 = [4,3,2,9,1,3,4]

r1 = es_capicua(vector1, 7)
r2 = es_capicua(vector2, 7)

print("R1: ", r1)
print("R2: ", r2)

