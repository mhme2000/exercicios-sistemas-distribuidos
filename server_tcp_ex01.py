import socket
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
def average(lst):
    return sum(lst) / len(lst)
def meanValue(list, avg):
    value = 0
    for c in list:
        absActual = abs(value - avg)
        absLoop = abs(c - avg)
        if(absLoop < absActual):
            value = c
    return value
list = []
con, cliente = tcp.accept()
print ('Conectado por', cliente)
while True:
    list.clear()
    for c in range(50):
        value = int(con.recv(1024))
        if (value == 0):
            con.close()
            break
        list.append(value)
    if (value == 0):
        break
    averageList = average(list)
    mean = meanValue(list, averageList)
    result = bytes(str(mean), 'utf-8')
    con.send(result)

