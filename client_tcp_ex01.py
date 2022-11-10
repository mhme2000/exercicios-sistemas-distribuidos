import socket
HOST = '192.168.18.153'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
msgEnum = print(
    '''
========================================================
1. Fazer um algoritmo para ler uma lista de 50 
   números e dizer qual valor existente na lista 
   que mais se aproxima do valor médio (a média) 
   dos elementos da própria lista.
========================================================
    '''
    )
while opt != 0:
    for c in range(50): 
        msg = input("Digite um valor: ").encode()
        tcp.send (msg)
    resp = (tcp.recv(1024)).decode()

    print(f'O valor que mais se aproxima da média da lista é: {resp}')
    opt = int(input("Digite [0] para interromper a execução do programa ou [1] para continuar: "))
    if(opt == 0):
        break
tcp.close()