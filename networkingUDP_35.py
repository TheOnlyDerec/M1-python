import socket
from struct import unpack
import json,pickle

# Création d'un socket UDP (SOCK_DGRAM)
UDPSock = socket.socket(type=socket.SOCK_DGRAM)
# Ecoute sur port 21567 à tous les IPs
# Attention si vous n'etes pas derriere une firewall, vous accepter TOUT LE MONDE
# C'est comme poster sa fete sur facebook en public...
listen_addr = (socket.gethostname(), 21567)
UDPSock.bind(listen_addr)

print("Setting UDP host {0}".format(listen_addr))

while True:
    # On attend un paquet de taille 1024 octets max

    data, addr = UDPSock.recvfrom(1024)

    if len(data) < 9:
        print("Message de {0} et trop courte".format(addr))
        continue

    #On attend le format "format_|_MSG
    fmtTokenized = data[:9].decode().split("_|_")

    if len(fmtTokenized) != 2:
        print(addr, " a envoyé n'importe quoi comme format du string binaire")
        continue

    if fmtTokenized[0] not in ["str", "json", "pickle", "pack"]:
        print("{0} a envoyé n'importe quoi comme format".format(addr))
        continue

    fmtTokenized = fmtTokenized[0]
    msgB = data[len(fmtTokenized) + 3:]

    try:
        if fmtTokenized == "str":
            print("{0}\nde\n{1}\n\n".format(msgB.decode(), addr))
        elif fmtTokenized == "pack":
            print("{0}\nde\n{1}\n\n".format(unpack(msgB.decode()), addr))
        elif fmtTokenized == "json":
            # Can work with binairies, but we will stick with ascii strings
            print("{0}\nde\n{1}\n\n".format(json.loads(msgB.decode()), addr))
        else:
            #We have already checked before that the format is ok
            print("{0}\nde\n{1}\n\n".format(pickle.loads(msgB), addr))
            # Pcikle works with binary data
    except:
        print(addr, " a envoyé n'importe quoi", "\n\n")
