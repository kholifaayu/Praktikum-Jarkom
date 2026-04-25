from socket import *

# definisikan port server
serverPort = 12000

# buat socket TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# bind socket ke port
serverSocket.bind(('', serverPort))

# listen untuk koneksi masuk
serverSocket.listen(1)
print('The server is ready to receive')


while True:
    # accept a connection
    connectionSocket, addr = serverSocket.accept()
    print('Connected by', addr)

    # receive message from client
    sentence = connectionSocket.recv(1024).decode()
    print('Received from client:', sentence)

    # convert message to uppercase
    modifiedSentence = sentence.upper()

    # send modified message back to client
    connectionSocket.send(modifiedSentence.encode())

    # close the connection
    connectionSocket.close()
    


