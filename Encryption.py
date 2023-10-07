def user_input():
    message = input(print("Enter message to encode"))
    conv(message)
    
def conv(message):
    array=[]
    for i in range (len(message)):
        array.append(int(ord(message[i])))
    DataMatrix=[]
    while len(array)>0:
        arr=[]
        if len(array)!=1:
            arr.append(array[0])
            array.pop(0)
            arr.append(array[0])
            array.pop(0)
        else:
            arr.append(array[0])
            array.pop(0)
            arr.append(0)
        DataMatrix.append(arr)
    print(DataMatrix)
    encode(DataMatrix)
    
def encode(DataMatrix):
    key=[[10,12],[2,4]]
    EncryptedMatrix=[]
    for i in range (len(DataMatrix)):
        encoded=[]
        encoded.append((key[0][0]*DataMatrix[i][0])+(key[1][0]*DataMatrix[i][1]))
        encoded.append((key[0][1]*DataMatrix[i][0])+(key[1][1]*DataMatrix[i][1]))
        EncryptedMatrix.append(encoded)
    print(EncryptedMatrix)
    decode(EncryptedMatrix,key)
    
def decode(EncryptedMatrix,key):
    determinant=((key[0][0]*key[1][1])-(key[1][0]*key[0][1]))
    oneoverdeterminant=1/determinant
    print(determinant)
    inversekey=[[key[1][1],(key[0][1])*-1],[(key[1][0])*-1,key[0][0]]]
    for i in range(len(inversekey)):
        inversekey[i][0]=inversekey[i][0]*oneoverdeterminant
        inversekey[i][1]=inversekey[i][1]*oneoverdeterminant
    print(inversekey)
    DecryptedMatrix=[]
    for i in range (len(EncryptedMatrix)):
        decoded=[]
        decoded.append(int((inversekey[0][0]*EncryptedMatrix[i][0])+(inversekey[1][0]*EncryptedMatrix[i][1])))
        decoded.append(int((inversekey[0][1]*EncryptedMatrix[i][0])+(inversekey[1][1]*EncryptedMatrix[i][1])))
        DecryptedMatrix.append(decoded)
    print(DecryptedMatrix)
    deconv(DecryptedMatrix)
    
def deconv(DecryptedMatrix):
    message=""
    for i in range(len(DecryptedMatrix)):
        message=message+chr(DecryptedMatrix[i][0])
        message=message+chr(DecryptedMatrix[i][1])
    print(message)     
###############################
user_input()


