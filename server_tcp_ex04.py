import socket
import statistics
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
def mode(lst):
    return statistics.multimode(lst)
list = []
con, cliente = tcp.accept()
print ('Conectado por', cliente)
while True:
    list.clear()
    for c in range(300):
        value = int(con.recv(1024))
        if (value == 0):
            con.close()
            break
        list.append(value)
    if (value == 0):
        break
    modeList = mode(list)
    result = bytes(str(modeList), 'utf-8')
    con.send(result)

