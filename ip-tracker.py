import bluetooth

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind(("", bluetooth.PORT_ANY))
server_socket.listen(1)
client_socket, address = server_socket.accept()
print("Accepted connection from", address)
data = client_socket.recv(1024)
print("Received data:", data)
with open("steal_data.txt", "wb") as file:
    file.write(data)
  client_socket.close()
server_socket.close()
