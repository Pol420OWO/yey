def run():
  print("Adios, mundo!")
  HOST = '172.16.22.82'
  PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
