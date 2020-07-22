 import socket
 import threading

 PORT = 5050
 SERVER = socket.gethostbyname(socket.gethostname())
 ADDR=(SERVER,PORT)
 server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 server.bind(ADDR)
 def handle_client(conn , addr ):
     pass
 def start():
    server.listen()
    while true:
            conn, addr= server.accept()
        thread = threading.Thread(target=handle_client,args=(conn , addr))
        thread.start()
        print("ACTIVE CONNECTIONS {threading.activeCount() - 1}")





print("[STARTING] the server is starting...")
start()



