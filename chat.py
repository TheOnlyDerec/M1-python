import socket

UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

data2 = 'str_|_      ***********                  ***********\n  *****************            *****************\n*********************        *********************\n***********************      ***********************\n************************    ************************\n*************************  *************************\n **************************************************\n  ************************************************\n    ********************************************\n      ****************************************\n         **********************************\n           ******************************\n              ************************\n                ********************\n                   **************\n                     **********\n                       ******\n                         **'
#addr = ("localhost", PC5565-111-00.meca.ingenierie.upmc.fr)
addr=(socket.gethostname(), 12345)
UDPSock.bind(addr)


while True :
    message = input('Msg :\n')
    UDPSock.sendto(message.encode(), addr)
    data, addr = UDPSock.recvfrom(1024)
    print(data.decode())

# #UDPSock.sendto(type.encode(),addr)
# UDPSock.sendto(data,addr)
