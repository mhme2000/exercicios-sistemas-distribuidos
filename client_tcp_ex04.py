import socket
HOST = '192.168.18.153'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
opt = 1
msgEnum = print(
    '''
========================================================
4. Fazer um algoritmo para ler uma lista de 300
números e dizer qual é a moda da lista (qualquer
uma entre as várias possíveis). A moda é o valor
que mais se repete na lista.
========================================================
    '''
    )
while opt != 0:
    for c in range(300): 
        msg = input("Digite um valor: ").encode()
        tcp.send (msg)
    resp = (tcp.recv(1024)).decode()

    print(f'A moda da lista de valores é: {resp}')
    opt = int(input("Digite [0] para interromper a execução do programa ou [1] para continuar: "))
    if(opt == 0):
        tcp.send(str(opt).encode())
        break
tcp.close()
print('Conexão interrompida pelo client!')
