from socket import *

#Start test()
def test():

    #Specify the port
    serverPort = 80
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('',serverPort))

    #Listen for the 1 connection
    
    serverSocket.listen(1)

    #Print the port address
    print("web server on port",serverPort)

    #Start thw while loop.
    while True:

        #Establish the connection.
        print("ready to serve")

        #Create connection socket for accepted client.
        connectionSocket,addr = serverSocket.accept()

        #Start the try block.
        try:

            #Recieve message.
            message = connectionSocket.recv(1024)

            #Print the connection message
            print(message)

            #Determine the filename
            filename = message.split()[1]
            #Print the file name
            print(filename[1])

            print(filename,'||',filename[1])

            #Open the file
            f = open(filename[1:])
            outputdata = f.read()

            #DEBUG to check output data
            print(outputdata)

            #Send one HTTP header line into socket
            connectionSocket.send("""HTTP/1.0 200 OK
                       Content-Type: text/html

                          <html>
                          <head>
                          <title>Success</title>
                          </head>
                          <body>
                          Your file Exist!
                          </body>
                           </html>
                             """.encode());

            #connectionSocket.send(outputdata)

            #connectionSocket.send(message)
            connectionSocket.close()


        #If IOError
        except IOError:

            #Send response message for the file not found.
            print ("404 Not Found")
            connectionSocket.send("""HTTP/1.0 404 Not Found\r\n""".encode());
            pass

        #Temp break
        break
pass

if __name__ =="__main__":
    test()