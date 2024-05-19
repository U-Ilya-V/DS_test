class ItemIsNotListError(Exception):
    pass

class EmptyListError(Exception):
    pass

class DiffrenLengthVectorsError(Exception):
    pass

class ZeroVectorError(Exception):
    pass

class DataTypeError(Exception):
    pass

def isCorrectData(v1, v2):
    if not((type(v1) is list) and (type(v2) is list)):
        raise ItemIsNotListError("one of the item is not a list")
    if len(v1)  == 0 or len(v2) == 0: 
        raise EmptyListError("one of the vectors is empty")
    if len(v1) != len(v2):    
        raise DiffrenLengthVectorsError("vectors have different length") 
    if all(item == 0 for item in v1) or all(item == 0 for item in v2):
        raise ZeroVectorError("one of vector is the zero vector")
    if not(all(isinstance(item,(int, float)) for item in v1)) or not(all(isinstance(item,(int, float)) for item in v2)):
        raise DataTypeError("not all elements of number")

def funcTest2 (v1, v2):
    try:
        isCorrectData(v1, v2)
    except (ItemIsNotListError, EmptyListError, DiffrenLengthVectorsError, ZeroVectorError, DataTypeError) as e:
        print(e)
    else:
        scalarProduct: float = 0
        lenVector1: float = 0
        lenVector2: float = 0
        for i in range(len(v1)):
            scalarProduct = scalarProduct + (v1[i]*v2[i])
            lenVector1 = lenVector1 + (v1[i] ** 2)
            lenVector2 = lenVector2 + (v2[i] ** 2)
        cosDist = 1 - (scalarProduct/((lenVector1 ** 0.5 )*(lenVector2** 0.5 )))
        return cosDist

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

print(funcTest2(a,b))

