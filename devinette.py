import socket

UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

addr=('PC5565-111-00.meca.ingenierie.upmc.fr', 21568)
listen_addr = (socket.gethostname(), 21568)
UDPSock.bind(listen_addr)

high = 1000000
low = -1000000
med = 0

msg = str(med)

UDPSock.sendto(msg.encode(),addr)
ret, addr = UDPSock.recvfrom(4096)
retour = int(ret.decode())

tent = 0

while not retour == 0:
    tent+=1
    if retour == 2:
        high = med
        med = int((med + low)/2)
    else:
        low = med
        med = int((med + high) / 2)
    msg = str(med)
    UDPSock.sendto(msg.encode(),addr)
    ret, addr = UDPSock.recvfrom(4096)
    retour = int(ret.decode())

print('Nombre trouvé : ' + msg + ' en ' + str(tent) + ' tentatives.')