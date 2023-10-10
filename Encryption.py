def user_input():
    message = input(print("Enter message to encode"))
    conv(message)
    
def conv(message):
    array=[]
    for i in range (len(message)): #Convert input characters to ASCII
        array.append(int(ord(message[i]))) #Add to temp array variable
    DataMatrix=[]
    while len(array)>0: #While there are characters in the array
        arr=[]
        if len(array)!=1: #If more than one character remaining
            arr.append(array[0]) #Adds to 1x2 matrix
            array.pop(0) #Removes from temp array
            arr.append(array[0])#Adds to 1x2 matrix
            array.pop(0)
        else: #If only one character
            arr.append(array[0]) #Append to 1x2 matrix
            array.pop(0)
            arr.append(0) #Adds filler to array to keep matrix 1x2 size
        DataMatrix.append(arr) #Appends all 1x2 matrices to datamatrix
    print(DataMatrix)
    encode(DataMatrix)
    
def encode(DataMatrix):
    key=[[10,12],[2,4]] #Predetermined key
    EncryptedMatrix=[]
    for i in range (len(DataMatrix)): #Encrypt each 1x2 matrices
        encoded=[]
        encoded.append((key[0][0]*DataMatrix[i][0])+(key[1][0]*DataMatrix[i][1])) #Encrypt using hill cipher style.
        encoded.append((key[0][1]*DataMatrix[i][0])+(key[1][1]*DataMatrix[i][1]))
        EncryptedMatrix.append(encoded)
    print(EncryptedMatrix)
    decode(EncryptedMatrix,key)
    
def decode(EncryptedMatrix,key): #Decoding using inverse of previous function
    determinant=((key[0][0]*key[1][1])-(key[1][0]*key[0][1])) #Calculate determinant needed for inverse matrix multiplication
    oneoverdeterminant=1/determinant #Inverse determinant
    print(determinant)
    inversekey=[[key[1][1],(key[0][1])*-1],[(key[1][0])*-1,key[0][0]]] #Inverse key for inverse multiplication
    for i in range(len(inversekey)): 
        inversekey[i][0]=inversekey[i][0]*oneoverdeterminant #Finial inverse key creation step
        inversekey[i][1]=inversekey[i][1]*oneoverdeterminant
    print(inversekey)
    DecryptedMatrix=[]
    for i in range (len(EncryptedMatrix)):
        decoded=[]
        decoded.append(int((inversekey[0][0]*EncryptedMatrix[i][0])+(inversekey[1][0]*EncryptedMatrix[i][1])))#Decrypt
        decoded.append(int((inversekey[0][1]*EncryptedMatrix[i][0])+(inversekey[1][1]*EncryptedMatrix[i][1])))
        DecryptedMatrix.append(decoded)
    print(DecryptedMatrix)
    deconv(DecryptedMatrix)
    
def deconv(DecryptedMatrix):
    message=""
    for i in range(len(DecryptedMatrix)):
        message=message+chr(DecryptedMatrix[i][0]) #Convert back to characters from ASCII
        message=message+chr(DecryptedMatrix[i][1])
    print(message)     
###############################
user_input()


