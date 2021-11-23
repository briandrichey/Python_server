# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET , SOCK_STREAM)
# Prepare a server socket on a particular port
# Fill in code to set up the port
HOST = '127.0.0.1'
PORT = 6789
serverSocket.bind((HOST,PORT))
serverSocket.listen(1)
while True :
    # Establish the connection
    print("Ready to serve ... ")
    connectionSocket , addr = serverSocket.accept() # Fill in code to get a connection
    try:
        message = input('Enter url: http://')# Fill in code to read GET request
        filename = message.split('/')[1]
         # Fill in security code
        if (filename == 'grades/'):
            print('\n Error 403: forbidden \n')
        f = open(filename)
        outputdata = f.read()# Fill in code to read data from the file
        # Send HTTP header line (s) into socket
        headerbytes= filename.encode('utf-8')
        serverSocket.send(headerbytes)# Fill in code to send header (s)
        # Send the content of the requested file to the client
        for i in range(0,len(outputdata)) :
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError :
        # Send response message for file not found
        if len(outputdata) == 0 :# Fill in
            print('\n Error 404: file not found \n')
        # Close client socket
        connectionSocket.close()# Fill in
serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data